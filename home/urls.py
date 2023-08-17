from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    # home
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_end/', views.signup_end, name='signup_end'),
    #mypage
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage_update/', views.mypage_update, name="mypage_update"),
    # path('password/', views.change_password, name='change_password'),
    path('change-password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)