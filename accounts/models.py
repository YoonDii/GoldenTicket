from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    kakao_id = models.BigIntegerField(null=True, unique=True)
    naver_id = models.CharField(null=True, unique=True, max_length=100)