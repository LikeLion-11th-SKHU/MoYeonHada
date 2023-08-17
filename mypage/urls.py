from django.contrib import admin
from django.urls import path
from . import views  # views가져오기

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # home
    path('my_posts_t/', views.my_posts_t, name="my_posts_t"),
    path('my_posts_s/', views.my_posts_s, name="my_posts_s"),
    path('my_posts_o/', views.my_posts_o, name="my_posts_o"),

    path('wishlist_t/', views.wishlist_t, name='wishlist_t'),
    path('wishlist_s/', views.wishlist_s, name='wishlist_s'),
    path('wishlist_o/', views.wishlist_o, name='wishlist_o'),

    path('add_to_wishlist_t/<int:t_post_id>/', views.add_to_wishlist_t, name='add_to_wishlist_t'),
    path('add_to_wishlist_s/<int:s_post_id>/', views.add_to_wishlist_s, name='add_to_wishlist_s'),
    path('add_to_wishlist_o/<int:o_post_id>/', views.add_to_wishlist_o, name='add_to_wishlist_o'),

    path('remove_from_wishlist_t/<int:t_post_id>/', views.remove_from_wishlist_t, name='remove_from_wishlist_t'),
    path('remove_from_wishlist_s/<int:s_post_id>/', views.remove_from_wishlist_s, name='remove_from_wishlist_s'),
    path('remove_from_wishlist_o/<int:o_post_id>/', views.remove_from_wishlist_o, name='remove_from_wishlist_o'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)