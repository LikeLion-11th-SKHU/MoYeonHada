from django.contrib import admin
# from .models import Bookmark
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.

# admin.site.register(Bookmark)
class Profileinline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (Profileinline)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)