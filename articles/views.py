from django.shortcuts import render, redirect
from .models import PlayDetail, LocationDetail


def main(request):
    play_list = PlayDetail.objects.filter(genrename="연극")
    musical_list = PlayDetail.objects.filter(genrename="뮤지컬")
    classic_list = PlayDetail.objects.filter(genrename="클래식")
    return render(
        request,
        "articles/main.html",
        {
            "playlist_rank": play_list[:3],
            "playlist": play_list[:6],
            "musical_list": musical_list[:6],
            "classic_list": classic_list[:6],
        },
    )


def index(request):
    return render(request, "articles/index.html")


def detail(request, performance_pk):
    performance = PlayDetail.objects.get(playid=performance_pk)
    location = LocationDetail.objects.get(locationid=performance.locationid)
    context = {
        "performance": performance,
        "location": location,
    }
    return render(request, "articles/detail.html", context)

def play(request):
    playlist = PlayDetail.objects.filter(genrename="연극")
    context = {"playlist": playlist}
    return render(request, "articles/play.html", context)

