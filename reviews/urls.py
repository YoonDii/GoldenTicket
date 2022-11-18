from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<str:performance_pk>/<int:review_pk>/update/", views.update, name="update"),
    path("<str:performance_pk>/<int:review_pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/comment_create/", views.comment_create, name="comment_create"),
    path("comment_delete/<int:pk>/", views.comment_delete, name="comment_delete"),
]
