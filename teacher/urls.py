from django.urls import path
from teacher import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # teacher
    path('main/', views.t_main, name = 't_main'),
    path('t_c/', views.t_c, name='t_c'),
    path('t_r/<int:pk>', views.t_r, name='t_r'),
    path('t_u/<int:pk>', views.t_u, name='t_u'),
    path('comment/<int:pk>', views.comment_create, name='comment_create'),
    path('comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)