from django.urls import path
from teacher import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # teacher
    path('main/', views.t_main, name = 't_main'),
    path('t_c/', views.t_c, name='t_c'),
    path('t_c/t_create', views.t_create, name='t_create'),
    path('t_r/<int:id>', views.t_r, name='t_r'),
    path('t_u/<int:id>', views.t_u, name='t_u'),
    path('t_update/<int:id>', views.t_update, name='t_update'),
    path('t_d/<int:id>', views.t_d, name='t_d'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)