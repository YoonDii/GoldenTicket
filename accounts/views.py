from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login


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
