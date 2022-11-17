from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.main, name="main"),
    path("search/", views.search, name="search"),
    path("articles/", views.index, name="index"),
    path("articles/d/<str:performance_pk>/", views.detail, name="detail"),
    path("articles/<str:performance_pk>/like/", views.like, name="like"),
    path("articles/ranking/", views.ranking, name="ranking"),
    # path("articles/play/", views.play, name="play"),
    # path("articles/musical/", views.musical, name="musical"),
    # path("articles/classic/", views.classic, name="classic"),
    # path("articles/dance/", views.dance, name="dance"),
    # path("articles/ktm/", views.ktm, name="ktm"),
]
