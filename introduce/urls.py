from django.urls import path
from introduce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # introduce
    path('main/', views.introduce_main, name = 'introduce_main')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)