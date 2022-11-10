from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


def index(request):

    return render(request, "accounts/index.html")


def signup(request):

    if request.method == "POST":
        sign_form = CustomUserCreationForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    else:
        sign_form = CustomUserCreationForm()

    context = {
        "sign_form": sign_form,
    }

    return render(request, "accounts/signup.html", context)


def login(request):

    login_form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect("accounts:index")
    else:
        login_form = AuthenticationForm()
    context = {
        "login_form": login_form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):

    auth_logout(request)
    return redirect("accounts:index")


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

    return render(request, "accounts/login.html", context)


def profile(request):

    user = request.user

    context = {
        "user_id": user.username,
        "user_email": user.email,
    }

    return render(request, "accounts/profile.html", context)
