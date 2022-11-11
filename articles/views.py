from django.shortcuts import render, redirect
from .models import PlayDetail


def main(request):
    playlist = PlayDetail.objects.all()
    return render(
        request,
        "articles/main.html",
        {
            "playlist": playlist[:1],
        },
    )


def index(request):
    return render(request, "articles/index.html")


def play(request):
    playlist = PlayDetail.objects.filter(genrename="연극")
    context = {"playlist": playlist}
    return render(request, "articles/play.html", context)
