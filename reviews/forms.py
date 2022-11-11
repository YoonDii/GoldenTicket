from django import forms
from .models import ReviewPhoto, Review, Comment
from django.forms import ClearableFileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "grade",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class ReviewPhotoForm(forms.ModelForm):
    class Meta:
        model = ReviewPhoto
        fields = ("image",)
        widgets = {
            "image": ClearableFileInput(attrs={"multiple": True}),
        }
        labels = {
            "image": "다중 클릭하여 사진을 여러장 올릴 수 있어요!",
        }
