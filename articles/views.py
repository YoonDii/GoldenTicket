from django.shortcuts import render, redirect
from .models import PlayDetail, LocationDetail
from django.http import JsonResponse
from reviews.forms import ReviewForm, ReviewPhotoForm, CommentForm
from reviews.models import ReviewPhoto, Review, Comment
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg, Count
from django.contrib import messages
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    today = datetime.date.today()

    play_list = (
        PlayDetail.objects.filter(genrename="연극")
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )
    musical_list = (
        PlayDetail.objects.filter(genrename="뮤지컬")
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )
    classic_list = (
        PlayDetail.objects.filter(genrename="클래식")
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )
    dance_list = (
        PlayDetail.objects.filter(genrename="무용")
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )
    ktm_list = (
        PlayDetail.objects.filter(genrename="국악")
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )

    return render(
        request,
        "articles/main.html",
        {
            "playlist_rank": play_list[:3],
            "musical_rank": musical_list[:3],
            "classic_rank": classic_list[:3],
            "dance_rank": dance_list[:3],
            "ktm_rank": ktm_list[:3],
            "playlist": play_list[:6],
            "musical_list": musical_list[:6],
            "classic_list": classic_list[:6],
            "dance_list": dance_list[:6],
            "ktm_list": ktm_list[:6],
        },
    )


def index(request):
    today = datetime.date.today()

    if request.GET.get("genre"):
        genre = request.GET.get("genre")

        playlist = (
            PlayDetail.objects.filter(genrename=genre)
            .exclude(playenddate__lte=today)
            .order_by("-playstdate")
        )
        plist = (
            PlayDetail.objects.filter(genrename=genre)
            .exclude(playenddate__lte=today)
            .order_by("playenddate")
        )
        totalnum = len(playlist)
        page1 = request.GET.get("page", 1)
        playlistpage = Paginator(playlist, 40)
        totalpagenum = playlistpage.num_pages

        try:
            news = playlistpage.page(page1)
        except PageNotAnInteger:
            news = playlistpage.page(1)
        except EmptyPage:
            news = playlistpage.page(playlistpage.num_pages)

        plistpage = Paginator(plist, 40)
        try:
            olds = plistpage.page(page1)
        except PageNotAnInteger:
            olds = plistpage.page(1)
        except EmptyPage:
            olds = plistpage.page(plistpage.num_pages)

        context = {
            "genrename": genre,
            "news": news,
            "olds": olds,
            "totalnum": totalnum,
            "totalpagenum": totalpagenum,
        }

    else:
        playlist = PlayDetail.objects.order_by("-playstdate")
        plist = PlayDetail.objects.order_by("playenddate")

        totalnum = len(playlist)
        page1 = request.GET.get("page", 1)
        playlistpage = Paginator(playlist, 40)

        try:
            news = playlistpage.page(page1)
        except PageNotAnInteger:
            news = playlistpage.page(1)
        except EmptyPage:
            news = playlistpage.page(playlistpage.num_pages)

        context = {
            "genrename": "모든 공연",
            "news": news,
            "totalnum": totalnum,
        }

    return render(request, "articles/index.html", context)


from urllib import parse


def detail(request, performance_pk):
    performance = PlayDetail.objects.get(playid=performance_pk)
    location = LocationDetail.objects.get(locationid=performance.locationid)
    reviews = Review.objects.order_by("-id")
    # -pk 순으로 출력하기 위해 따로 comments 만들어서 넘겨줌
    ticketurl = parse.quote(performance.playname)
    comments = Comment.objects.filter(review__playId=performance).order_by("-id")
    users = User.objects.all()
    review_photo = ReviewPhoto.objects.all()

    starlists = Review.objects.filter(playId=performance.id)
    Avg_grade = 0
    if starlists:
        for starlist in starlists:
            Avg_grade += int(starlist.grade)
        Avg_grade = round(Avg_grade / len(starlists), 1)

    # Comment Detail
    comment_form = CommentForm()
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
            return redirect("articles:detail", performance_pk)
    else:
        review_form = ReviewForm()
        reviewPhoto_form = ReviewPhotoForm()
    context = {
        "performance": performance,
        "location": location,
        "users": users,
        "reviews": reviews,
        "review_photos": review_photo,
        "review_form": review_form,
        "reviewPhoto_form": reviewPhoto_form,
        "comment_form": comment_form,
        "Avg_grade": Avg_grade,
        "comments": comments,
        "ticketurl": ticketurl,
    }
    return render(request, "articles/detail.html", context)


# like
def like(request, performance_pk):
    if request.user.is_authenticated:
        performance = PlayDetail.objects.get(playid=performance_pk)
        if performance.like_users.filter(pk=request.user.id).exists():
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


def search(request):
    print(request.GET)
    all_data = PlayDetail.objects.order_by("-id")
    search = request.GET.get("search")

    if search:
        if len(search) > 1:
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
            return render(request, "articles/search.html", context)
        else:
            context = {
                "search": search,
                "search_list": "",
            }
    else:
        context = {
            "search": "",
            "search_list": "",
        }

    return render(request, "articles/search.html", context)


def ranking(request):
    today = datetime.date.today()
    play_list = (
        PlayDetail.objects.all()
        .annotate(hot=Count("like_users"))
        .exclude(playenddate__lte=today)
        .order_by("-hot")
    )
    return render(
        request,
        "articles/ranking.html",
        {
            "play_list_best": play_list[:3],
            "play_list": play_list[3:50],
            "today": today,
        },
    )
