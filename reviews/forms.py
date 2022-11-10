from django import forms
from .models import ReviewPhoto, Review, Comment


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
