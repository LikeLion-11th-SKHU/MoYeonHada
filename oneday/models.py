from django.db import models

# Create your models here.
class OnedayRecruit(models.Model):
    number = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    region = models.CharField(max_length=50, default='')
    hashtag = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    content = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

class OnedayApply(models.Model):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    people = models.CharField(max_length=50)
    memo = models.CharField(max_length=50)

    def __str__(self):
        return self.username