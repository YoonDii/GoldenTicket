from django.db import models
from django.conf import settings

# Create your models here.


class PlayDetail(models.Model):
    playid = models.CharField(max_length=20)
    playname = models.CharField(max_length=50)
    genrename = models.CharField(max_length=20)
    playstate = models.CharField(max_length=20)
    playstdate = models.CharField(max_length=20)
    playenddate = models.CharField(max_length=20)
    poster = models.ImageField(upload_to="images/", blank=True)
    locationname = models.CharField(max_length=30)
    playcast = models.CharField(max_length=50)
    runtime = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    locationid = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to="images/", blank=True)
    image2 = models.ImageField(upload_to="images/", blank=True)
    image3 = models.ImageField(upload_to="images/", blank=True)
    image4 = models.ImageField(upload_to="images/", blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="performance"
    )


class LocationDetail(models.Model):
    locationid = models.CharField(max_length=20)
    locationname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    relateurl = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lgt = models.CharField(max_length=10)
