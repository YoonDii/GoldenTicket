from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.main, name="main"),
    path("articles/", views.index, name="index"),
    path("articles/play/", views.play, name="play"),
]
