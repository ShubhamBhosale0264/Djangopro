from playsinkpro import settings
from django.conf.urls.static import static
from django.urls import path
from playsinkapp import views
from django.contrib import admin
admin.site.site_header = "Welcome Shuhbham to PlaysinkPro"
admin.site.index_title = "Admin Database"



urlpatterns = [
    path('home',views.home),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('playlist',views.playlist),
    path('artist',views.artist),
    path('genre',views.genre_songs),
    path('about',views.about),
    path('add_to_playlist/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('cookies',views.cooki),
    path('legal',views.lgl),
    path('privacy',views.privacy),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MUSIC_URL, document_root=settings.MUSIC_ROOT)  
