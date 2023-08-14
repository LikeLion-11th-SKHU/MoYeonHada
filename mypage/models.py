from django.conf import settings
from django.db import models

class WishlistItem(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    withdrawal_date = models.DateTimeField(null=True, blank=True)
    is_vaild = models.BooleanField(default=True)