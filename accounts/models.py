from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    kakao_id = models.BigIntegerField(null=True, unique=True)
    naver_id = models.CharField(null=True, unique=True, max_length=100)
    image = ProcessedImageField(
        upload_to="media/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 80},
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    def profile_image(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        else:
            return "https://postfiles.pstatic.net/MjAyMDExMDFfMTA1/MDAxNjA0MjI4ODc1Mzk0.05ODadJdsa3Std55y7vd2Vm8kxU1qScjh5-3eVJ9T-4g.h7lHansSdReVq7IggiFAc44t2W_ZPTPoZWihfRMB_TYg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EB%9E%91.jpg?type=w773"
