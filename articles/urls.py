from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.main, name="main"),
    path("search/", views.search, name="search"),
    path("articles/", views.index, name="index"),
    path("articles/d/<str:performance_pk>/", views.detail, name="detail"),
    path("articles/<str:performance_pk>/like/", views.like, name="like"),
]
