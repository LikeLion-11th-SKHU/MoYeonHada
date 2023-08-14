from django.db import models
from django.conf import settings

# Create your models here.

class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Teachers')
    
    title = models.CharField(max_length=50, null=False, blank = False,)
    number = models.PositiveIntegerField()
    content = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    period1 = models.DateField(default='',max_length=50, null=False, blank = False,)
    period2 = models.DateField(default='',max_length=50, null=False, blank = False,)
    region = models.CharField(default='',max_length=50, null=False, blank = False,)
    
    FIELD_T = (('휴대전화', '휴대전화'), ('인터넷', '인터넷'), ('키오스크', '키오스크'), ('생활편의', '생활편의'), ('기타', '기타'))
    
    field = models.CharField(max_length=20, choices=FIELD_T, default='')
    
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Comments')
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Comments')
    
    content = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content