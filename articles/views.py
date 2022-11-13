from django.shortcuts import render, redirect
from .models import PlayDetail, LocationDetail
from django.http import JsonResponse


def main(request):
    play_list = PlayDetail.objects.filter(genrename="연극")
    musical_list = PlayDetail.objects.filter(genrename="뮤지컬")
    classic_list = PlayDetail.objects.filter(genrename="클래식")
    return render(
        request,
        "articles/main.html",
        {
            "playlist_rank": play_list[:3],
            "musical_rank": musical_list[:3],
            "classic_rank": classic_list[:3],
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


# like
def like(request, performance_pk):
    if request.user.is_authenticated:
        performance = PlayDetail.objects.get(playid=performance_pk)
        if performance.like_users.filter(pk=request.user.pk).exists():
            performance.like_users.remove(request.user)
            is_liked = False
        else:
            performance.like_users.add(request.user)
            is_liked = True
    else:
        return redirect("articles:detail", performance_pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": performance.like_users.count(),
        }
    )


def play(request):
    playlist = PlayDetail.objects.filter(genrename="연극").order_by("-playstdate")
    plist = PlayDetail.objects.filter(genrename="연극").order_by("playenddate")
    context = {"playlist": playlist, "plist": plist}
    return render(request, "articles/play.html", context)


def musical(request):
    playlist = PlayDetail.objects.filter(genrename="뮤지컬").order_by("-playstdate")
    plist = PlayDetail.objects.filter(genrename="뮤지컬").order_by("playenddate")
    context = {"playlist": playlist, "plist": plist}
    return render(request, "articles/musical.html", context)


def classic(request):
    playlist = PlayDetail.objects.filter(genrename="클래식").order_by("-playstdate")
    plist = PlayDetail.objects.filter(genrename="클래식").order_by("playenddate")
    context = {"playlist": playlist, "plist": plist}
    return render(request, "articles/classic.html", context)


def dance(request):
    playlist = PlayDetail.objects.filter(genrename="무용").order_by("-playstdate")
    plist = PlayDetail.objects.filter(genrename="무용").order_by("playenddate")
    context = {"playlist": playlist, "plist": plist}
    return render(request, "articles/dance.html", context)


def ktm(request):
    playlist = PlayDetail.objects.filter(genrename="국악").order_by("-playstdate")
    plist = PlayDetail.objects.filter(genrename="국악").order_by("playenddate")
    context = {"playlist": playlist, "plist": plist}
    return render(request, "articles/ktm.html", context)
