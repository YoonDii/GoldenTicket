from django.shortcuts import render, redirect
from .forms import ReviewForm, ReviewPhotoForm, CommentForm
from articles.models import PlayDetail
from .models import ReviewPhoto, Review


def index(request):

    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
    }

    return render(request, "reviews/index.html", context)


def create(request):

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
            return redirect("review:index")
    else:
        review_form = ReviewForm()
        reviewPhoto_form = ReviewPhotoForm()
    context = {
        "review_form": review_form,
        "reviewPhoto_form": reviewPhoto_form,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):

    review = Review.objects.get(pk=pk)
    # review_photos = ReviewPhoto.objects.filter(review=review)

    context = {
        "review": review,
        # "review_photos": review_photos,
    }

    return render(request, "reviews/detail.html", context)
