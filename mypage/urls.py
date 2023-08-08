from django.contrib import admin
from django.urls import path
from mypage import views  #mypage에 있는 views가져오기


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # home
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
    path('list/', views.list, name='list'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)