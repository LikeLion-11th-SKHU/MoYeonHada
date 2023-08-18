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
    path('t_comment/<int:pk>', views.t_comment_create, name='t_comment_create'),
    path('t_comment/<int:comment_pk>/delete', views.t_comment_delete, name='t_comment_delete'),
    path('search/', views.teacher_search, name='teacher_search'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)