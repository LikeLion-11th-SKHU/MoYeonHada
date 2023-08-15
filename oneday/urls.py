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
        path('o_comment/<int:pk>', views.o_comment_create, name='o_comment_create'),
        path('o_comment/<int:comment_pk>/edit', views.o_comment_edit, name='o_comment_edit'),
        path('o_comment/<int:comment_pk>/delete', views.o_comment_delete, name='o_comment_delete'),
        path('review/<int:pk>', views.review_create, name='review_create'),
        path('review/<int:review_pk>/edit', views.review_edit, name='review_edit'),
        path('review/<int:review_pk>/delete', views.review_delete, name='review_delete'),
        path('summernote/', include(summernote_urls)),
        path('hashtag/<str:hashtag>/', views.hashtag, name='hashtag'),
        path('search/', views.oneday_search, name='oneday_search'),
        
        
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)