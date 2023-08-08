from django.urls import path 
from oneday.views import oneday_main, oneday_new, oneday_create, oneday_read, oneday_detail, oneday_delete, oneday_edit, oneday_update
from django.conf.urls.static import static


urlpatterns = [
    # oneday
    path('main/', oneday_main, name = 'oneday_main'),
    path('new/', oneday_new, name = 'oneday_new'), 
    path('new/create/', oneday_create, name = 'oneday_create'), 
    path('read/', oneday_read, name = 'oneday_read'), 
    path('read/update/', oneday_read, name = 'oneday_update'),
    path('detail/<str:id>/', oneday_detail, name = 'oneday_detail'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)