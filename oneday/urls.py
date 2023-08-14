from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_summernote import views as django_summernote_views
from django_summernote import urls as summernote_urls

urlpatterns = [
        path('main/', views.oneday_main, name = 'oneday_main'),
        path('oneday_create/', views.oneday_create, name='oneday_create'),
        path('oneday_read/<int:pk>', views.oneday_read, name='oneday_read'),
        path('oneday_update/<int:pk>', views.oneday_update, name='oneday_update'),
        path('oneday_apply/<int:pk>/', views.oneday_apply, name='oneday_apply'),
        path('comment/<int:pk>', views.comment_create, name='comment_create'),
        path('comment/<int:comment_pk>/edit', views.comment_edit, name='comment_edit'),
        path('comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
        path('review/<int:pk>', views.review_create, name='review_create'),
        path('review/<int:review_pk>/edit', views.review_edit, name='review_edit'),
        path('review/<int:review_pk>/delete', views.review_delete, name='review_delete'),
        path('summernote/', include(summernote_urls)),
        path('hashtag/<str:hashtag>/', views.hashtag, name='hashtag'),
        path('search/', views.oneday_search, name='oneday_search'),
        
        
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)