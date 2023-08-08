from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #현 계정의 사용자를 가져올 수 ㅇ
    nickname = models.CharField(max_length = 64)
    profile_photo = modelsImageField(blank = True)


