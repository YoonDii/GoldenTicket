from django.shortcuts import render, redirect
from .models import PlayDetail, LocationDetail


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


def detail(request, performance_pk):
    performance = PlayDetail.objects.get(playid=performance_pk)
    location = LocationDetail.objects.get(locationid=performance.locationid)
    context = {
        "performance": performance,
        "location": location,
    }
    return render(request, "articles/detail.html", context)
