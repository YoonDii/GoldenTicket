from django.db import models
from django.conf import settings
from articles.models import PlayDetail


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    grades = [
        ("1", "⭐"),
        ("2", "⭐⭐"),
        ("3", "⭐⭐⭐"),
        ("4", "⭐⭐⭐⭐"),
        ("5", "⭐⭐⭐⭐⭐"),
    ]
    grade = models.CharField(max_length=20, choices=grades, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    playId = models.ForeignKey(PlayDetail, on_delete=models.CASCADE)


class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
