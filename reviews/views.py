from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, ReviewPhotoForm, CommentForm
from articles.models import PlayDetail
from .models import ReviewPhoto, Review, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse


def index(request):

    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
    }

    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    # 임시로 넣음
    play = PlayDetail.objects.get(pk=1)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        reviewPhoto_form = ReviewPhotoForm(request.POST, request.FILES)
        # 추후 pk 부분 수정해야 함
        playId = PlayDetail.objects.get(pk=1)

        images = request.FILES.getlist("image")
        if review_form.is_valid() and reviewPhoto_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.playId = playId
            if len(images):
                for image in images:
                    image_instance = ReviewPhoto(review=review, image=image)
                    review.save()
                    image_instance.save()
            else:
                review.save()
            # return redirect("articles:concert")
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
        reviewPhoto_form = ReviewPhotoForm()
    context = {
        "review_form": review_form,
        "reviewPhoto_form": reviewPhoto_form,
        "play": play,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):

    review = Review.objects.get(pk=pk)
    comments = Comment.objects.filter(review=review).order_by("-pk")
    comment_form = CommentForm()

    context = {
        "review": review,
        "comment_form": comment_form,
        "comments": comments,
    }

    return render(request, "reviews/detail.html", context)


@login_required
def update(request, performance_pk, review_pk):
    play = PlayDetail.objects.get(playid=performance_pk)
    review = Review.objects.get(pk=review_pk)
    photos = ReviewPhoto.objects.filter(review=review)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        reviewPhoto_form = ReviewPhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")
        for photo in photos:
            if photo.image:
                photo.delete()
        if review_form.is_valid():
            review = review_form.save(commit=False)
            if len(images):
                for image in images:
                    image_instance = ReviewPhoto(review=review, image=image)
                    review.save()
                    image_instance.save()
            else:
                review.save()
            review.save()
            return redirect("articles:detail", performance_pk)
    else:
        review_form = ReviewForm(instance=review)
    if photos:
        reviewPhoto_form = ReviewPhotoForm(instance=photos[0])
    else:
        reviewPhoto_form = ReviewPhotoForm()

    context = {
        "review_form": review_form,
        "reviewPhoto_form": reviewPhoto_form,
        "play": play,
    }

    return render(request, "reviews/create.html", context)


@login_required
def delete(request, performance_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    performance = get_object_or_404(PlayDetail, playid=performance_pk)
    if request.user == review.user:
        review = Review.objects.get(pk=review_pk)
        review.delete()
        return redirect("articles:detail", performance_pk)
    else:
        return render(
            request,
            "articles/detail.html",
            {
                "performance": performance,
                "review": review,
            },
            performance_pk,
        )


def comment_create(request, pk):
    print(request.POST)
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    print("실행되나?")
    user = request.user.pk
    temp = Comment.objects.filter(review_id=pk).order_by("-pk")
    comment_data = []

    for tem in temp:
        comment_data.append(
            {
                "user_pk": tem.user_id,
                "userName": tem.user.username,
                "content": tem.content,
                "commentPk": tem.pk,
                "commentDate": tem.created_at.strftime("%y-%m-%d"),
            }
        )
    context = {
        "comment_data": comment_data,
        "review_pk": review.pk,
        "user": user,
    }
    print(context)
    return JsonResponse(context)


# def comment_update(request, pk):

#     comment = Comment.objects.get(pk=pk)
#     review = comment.review
#     print(review)

#     if request.method == "POST":
#         comment_form = CommentForm(request.POST, instance=comment)
#         if comment_form.is_valid():
#             comment_form.save()
#             return redirect("reviews:detail", review.pk)

#     else:
#         comment_form = CommentForm(instance=comment)

#     context = {
#         "comment_form" : comment_form,
#     }

#     return redirect("reviews:detail", context)


def comment_delete(request, pk):
    print(request.POST)
    comment = Comment.objects.get(pk=pk)
    review = comment.review
    comment.delete()

    user = request.user.pk
    temp = Comment.objects.filter(review=review).order_by("-pk")
    comment_data = []

    for tem in temp:
        comment_data.append(
            {
                "user_pk": tem.user_id,
                "userName": tem.user.username,
                "content": tem.content,
                "commentPk": tem.pk,
                "commentDate": tem.created_at.strftime("%y-%m-%d"),
            }
        )
    context = {
        "comment_data": comment_data,
        "review_pk": review.pk,
        "user": user,
    }
    print("실행")
    return JsonResponse(context)
