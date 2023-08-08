from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저 모델
class Oneday(models.AbstractUser):
    # ... (나머지 모델 정의)

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)