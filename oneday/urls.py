from django.urls import path 
from oneday import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main/', views.oneday_main, name='oneday_main'),
    path('main/create', views.oneday_create, name='oneday_create'),
    path('main/create/apply/', views.oneday_apply_create, name='oneday_apply_create'), 
    path('main/create/recruit/', views.oneday_recruit_create, name='oneday_recruit_create'), 
    path('read/apply/', views.oneday_apply_read, name='oneday_apply_read'), 
    path('read/recruit/', views.oneday_recruit_read, name='oneday_recruit_read'), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)