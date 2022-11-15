from django.shortcuts import render, redirect
from .models import PlayDetail, LocationDetail
from django.http import JsonResponse
from reviews.forms import ReviewForm, ReviewPhotoForm, CommentForm
from reviews.models import ReviewPhoto, Review, Comment
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime,timedelta
from django.utils.dateformat import DateFormat
# from django.utils import timezone




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
# 날짜계산
# startdate = DateFormat(datetime.today()).format('Y.m.d')
# date = "playenddate" >= startdate
# print(startdate,date) # 2022.11.15 True

def index(request):
    # while date == True:
        if request.GET.get("genre"):
            genre = request.GET.get("genre")
            
            playlist = PlayDetail.objects.filter(
                genrename=genre,
            ).order_by("-playstdate")
            plist = PlayDetail.objects.filter(genrename=genre).order_by("playenddate")

            context = {
                "genrename": genre,
                "playlist": playlist,
                "plist": plist,
            }
            
        else:
            playlist = PlayDetail.objects.order_by("-playstdate")
            plist = PlayDetail.objects.order_by("playenddate")

            context = {
                "genrename": "모든 공연",
                "playlist": playlist,
                "plist": plist,
            }
                
        return render(request, "articles/index.html", context)


def detail(request, performance_pk):
    performance = PlayDetail.objects.get(playid=performance_pk)
    location = LocationDetail.objects.get(locationid=performance.locationid)
    reviews = Review.objects.order_by("-pk")
    users = User.objects.all()
    review_photo = ReviewPhoto.objects.all()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        reviewPhoto_form = ReviewPhotoForm(request.POST, request.FILES)

        images = request.FILES.getlist("image")
        if review_form.is_valid() and reviewPhoto_form.is_valid():
            review = review_form.save(commit=False)
            review.title = performance.playname
            review.user = request.user
            review.playId = performance
            if len(images):
                for image in images:
                    image_instance = ReviewPhoto(review=review, image=image)
                    review.save()
                    image_instance.save()
            else:
                review.save()
            # return redirect("articles:concert")
            return redirect("articles:detail", performance_pk)
    else:
        review_form = ReviewForm()
        reviewPhoto_form = ReviewPhotoForm()
    context = {
        "performance": performance,
        "location": location,
        "review_form": review_form,
        "reviewPhoto_form": reviewPhoto_form,
        "reviews": reviews,
        "users": users,
        "review_photos": review_photo,
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


# def play(request):
#     playlist = PlayDetail.objects.filter(genrename="연극").order_by("-playstdate")
#     plist = PlayDetail.objects.filter(genrename="연극").order_by("playenddate")
#     context = {"playlist": playlist, "plist": plist}
#     return render(request, "articles/play.html", context)


# def musical(request):
#     playlist = PlayDetail.objects.filter(genrename="뮤지컬").order_by("-playstdate")
#     plist = PlayDetail.objects.filter(genrename="뮤지컬").order_by("playenddate")
#     context = {"playlist": playlist, "plist": plist}
#     return render(request, "articles/musical.html", context)


# def classic(request):
#     playlist = PlayDetail.objects.filter(genrename="클래식").order_by("-playstdate")
#     plist = PlayDetail.objects.filter(genrename="클래식").order_by("playenddate")
#     context = {"playlist": playlist, "plist": plist}
#     return render(request, "articles/classic.html", context)


# def dance(request):
#     playlist = PlayDetail.objects.filter(genrename="무용").order_by("-playstdate")
#     plist = PlayDetail.objects.filter(genrename="무용").order_by("playenddate")
#     context = {"playlist": playlist, "plist": plist}
#     return render(request, "articles/dance.html", context)


# def ktm(request):
#     playlist = PlayDetail.objects.filter(genrename="국악").order_by("-playstdate")
#     plist = PlayDetail.objects.filter(genrename="국악").order_by("playenddate")
#     context = {"playlist": playlist, "plist": plist}
#     return render(request, "articles/ktm.html", context)


def search(request):
    all_data = PlayDetail.objects.order_by("-pk")
    search = request.GET.get("search")

    if search:
        search_list = all_data.filter(
            Q(playname__icontains=search)
            | Q(genrename__icontains=search)
            | Q(locationname__icontains=search)
            | Q(playcast__icontains=search)
        )
        context = {
            "search": search,
            "search_list": search_list,
        }
    else:
        context = {
            "search": search,
            "search_list": all_data,
        }

    return render(request, "articles/search.html", context)
