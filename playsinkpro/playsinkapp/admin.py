from django.contrib import admin
from .models import song_Genre, Song_Artist, Song, Playlist

class song_GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'song_name', 'artist_name']

class song_ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'song_name']

class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'artist_name', 'album_name', 'length', 'song_genre']

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(song_Genre, song_GenreAdmin)
admin.site.register(Song_Artist, song_ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)
