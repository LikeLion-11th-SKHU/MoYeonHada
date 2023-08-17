from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', views.s_main, name = 's_main'),
    path('s_c/', views.s_c, name='s_c'),
    path('s_r/<int:pk>', views.s_r, name='s_r'),
    path('s_u/<int:pk>', views.s_u, name='s_u'),
    path('s_comment/<int:pk>', views.s_comment_create, name='s_comment_create'),
    path('s_comment/<int:comment_pk>/delete', views.s_comment_delete, name='s_comment_delete'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)