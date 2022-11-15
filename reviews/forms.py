from django import forms
from .models import ReviewPhoto, Review, Comment
from django.forms import ClearableFileInput, Textarea, TextInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "content",
            "grade",
        ]
        labels = {
            "content": "관람후기",
            "grade": "별점",
        }
        widgets = {
            "content": Textarea(
                attrs={
                    "placeholder": "후기를 작성해주세요.",
                }
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": "",
        }
        widgets = {
            "content": TextInput(
                attrs={
                    "placeholder": "댓글 달기",
                }
            )
        }


class ReviewPhotoForm(forms.ModelForm):
    class Meta:
        model = ReviewPhoto
        fields = ("image",)
        widgets = {
            "image": ClearableFileInput(
                attrs={
                    "multiple": True,
                    "id": "image_field",
                    "style": "height: 100px; width: 100px; border: 1px dashed #adb5bd; color: #adb5bd;",
                }
            ),
        }
        labels = {
            "image": "다중 클릭하여 사진을 여러장 올릴 수 있어요!",
        }
