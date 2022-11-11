from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import requests



def index(request):
    return render(request, "accounts/index.html")


def signup(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                return redirect("accounts:index")
        else:
            signup_form = CustomUserCreationForm()

        context = {
            "form": signup_form,
        }

        return render(request, "accounts/signup.html", context)
    else:
        # 이미 로그인된 상태입니다 메시지 띄우기
        return redirect("accounts:index")


def login(request):

    if not request.user.is_authenticated:
        login_form = AuthenticationForm(request, data=request.POST)
        if request.method == "POST":
            if login_form.is_valid():
                auth_login(request, login_form.get_user())
                return redirect("accounts:index")
        else:
            login_form = AuthenticationForm()
        context = {
            "form": login_form,
        }
        return render(request, "accounts/login.html", context)
    else:
        # 이미 로그인된 상태입니다 메시지 띄우기
        return redirect("accounts:index")


def logout(request):

    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):

    if request.method == "POST":
        user_update_form = CustomUserChangeForm(request.POST, instance=request.user)

        if user_update_form.is_valid():
            user_update_form.save()
            return redirect("accounts:index")
    else:
        user_update_form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": user_update_form,
    }

    return render(request, "accounts/form.html", context)


@login_required
def profile(request):

    user = request.user

    context = {
        "user_id": user.username,
        "user_email": user.email,
    }

    return render(request, "accounts/profile.html", context)


@login_required
def pw_change(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:profile")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }

    return render(request, "accounts/form.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)

    return redirect("accounts:index")

# 소셜로그인
import secrets

state_token = secrets.token_urlsafe(16)


def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    redirect_uri = "http://localhost:8000/accounts/login/kakao/callback"
    client_id = "72b73a1d5e11f6c8e5ebb51f86c0dfab"  # 배포시 보안적용 해야함
    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")


def kakao_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "72b73a1d5e11f6c8e5ebb51f86c0dfab",  # 배포시 보안적용 해야함
        "redirect_uri": "http://localhost:8000/accounts/login/kakao/callback",
        "code": request.GET.get("code"),
    }
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

    headers = {"Authorization": f"bearer ${access_token}"}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()

    kakao_id = kakao_user_information["id"]
    kakao_nickname = kakao_user_information["properties"]["nickname"]
    kakao_profile_image = kakao_user_information["properties"]["profile_image"]

    if get_user_model().objects.filter(kakao_id=kakao_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    else:
        kakao_login_user = get_user_model()()
        kakao_login_user.username = kakao_nickname
        kakao_login_user.kakao_id = kakao_id
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get("next") or "accounts:index")


def naver_request(request):
    naver_api = "https://nid.naver.com/oauth2.0/authorize?response_type=code"
    client_id = "mwAzJRdaHS860HumilZ7"  # 배포시 보안적용 해야함
    redirect_uri = "http://localhost:8000/accounts/login/naver/callback"
    state_token = secrets.token_urlsafe(16)
    return redirect(
        f"{naver_api}&client_id={client_id}&redirect_uri={redirect_uri}&state={state_token}"
    )


def naver_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "mwAzJRdaHS860HumilZ7",  # 배포시 보안적용 해야함
        "client_secret": "Aa7AEd9pZ6",
        "code": request.GET.get("code"),
        "state": request.GET.get("state"),
        "redirect_uri": "http://localhost:8000/accounts/login/naver/callback",
    }
    naver_token_request_url = "https://nid.naver.com/oauth2.0/token"
    access_token = requests.post(naver_token_request_url, data=data).json()[
        "access_token"
    ]

    headers = {"Authorization": f"bearer {access_token}"}
    naver_call_user_api = "https://openapi.naver.com/v1/nid/me"
    naver_user_information = requests.get(naver_call_user_api, headers=headers).json()

    naver_id = naver_user_information["response"]["id"]
    naver_nickname = naver_user_information["response"]["nickname"]

    if get_user_model().objects.filter(naver_id=naver_id).exists():
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    else:
        naver_login_user = get_user_model()()
        naver_login_user.username = naver_nickname
        naver_login_user.naver_id = naver_id
        naver_login_user.set_password(str(state_token))
        naver_login_user.save()
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    auth_login(request, naver_user, backend="django.contrib.auth.backends.ModelBackend")

    return redirect(request.GET.get("next") or "accounts:index")