from django.db import models

# Create your models here.

class Teacher(models.Model):
    title = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    content = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    field = models.CharField(default='' ,max_length=50)
    period1 = models.CharField(default='',max_length=50)
    period2 = models.CharField(default='',max_length=50)
    region = models.CharField(default='',max_length=50)
    def __str__(self):
        return self.title