
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


def concert(request):
    concert = PlayDetail.objects.all()
    context = {"concert": concert}
    return render(request, "articles/concert.html", context)
