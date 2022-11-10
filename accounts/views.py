from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


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

        return render(request, "accounts/form.html", context)
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
        return render(request, "accounts/form.html", context)
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
            return redirect("accounts:profile")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }

    return render(request, "accounts/form.html", context)
