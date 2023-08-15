from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.

class OnedayCreate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    title = models.CharField(max_length=50, null=False, blank = False,)
    number = models.PositiveIntegerField()
    content = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    period1 = models.DateField(default=date(2023, 8, 10))
    period2 = models.DateField(default=date(2023, 8, 15))
    region = models.CharField(default='',max_length=50, null=False, blank = False,)
    hashtags = models.ManyToManyField('Hashtag')

    FIELD_T = (('공예', '공예'), ('요리', '요리'), ('미술', '미술'), ('운동', '운동'), ('음악', '음악'), ('기타', '기타'))
    
    field = models.CharField(max_length=20, choices=FIELD_T, default='')
    
    
    def __str__(self):
        return self.title
    
class OnedayApply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    name = models.CharField(max_length=50, null=False, blank = False,)
    phone = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    memo = models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    oneday = models.ForeignKey(OnedayCreate, on_delete=models.CASCADE)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    content = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    

class Review(models.Model):
    oneday = models.ForeignKey(OnedayCreate, on_delete=models.CASCADE)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    content = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

    
class Hashtag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.tag