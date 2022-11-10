from django.shortcuts import render
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
    return render(request, "articles/concert.html")
