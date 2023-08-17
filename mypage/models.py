from django.conf import settings
from django.db import models

from teacher.models import Teacher
from student.models import Student
from oneday.models import OnedayCreate

#teacher 
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='wishlists', null=False)
    t_post = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)
#student
class WishlistStudent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='wishlists_s', null=False)
    s_post = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)
#oneday
class WishlistOneday(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='wishlists_o', null=False)
    o_post = models.ForeignKey(OnedayCreate, on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)