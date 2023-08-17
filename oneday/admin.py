from django.contrib import admin

from .models import OnedayCreate, OnedayApply, OnedayHashtag

admin.site.register(OnedayCreate)
admin.site.register(OnedayApply)
admin.site.register(OnedayHashtag)