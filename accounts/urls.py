from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("<int:user_pk>/", views.profile, name="profile"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("password/", views.pw_change, name="pw_change"),
    path("delete/", views.delete, name="delete"),
    path("login/kakao/", views.kakao_request, name="kakao"),
    path("login/kakao/callback/", views.kakao_callback),
    path("login/naver/", views.naver_request, name="naver"),
    path("login/naver/callback/", views.naver_callback),
    path('blockuser/', views.blockuser, name='blockuser'),
    path('<int:user_pk>/block/', views.block, name='block'),
    path('<int:pk>/block_user_block', views.block_user_block, name='block_user_block'),
]
