from django.db import models
from django.contrib.auth.models import User

class song_Genre(models.Model):
    name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        return self.song_name
        return self.artist_name
    


class song_Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    def __str__(self):
        return self.artist_name
        return self.song_name

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    artist_name = models.ForeignKey(song_Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    length = models.DurationField()
    song_genre = models.ForeignKey(song_Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.self_title
        return self.artist_name
        return self.album_name
        return self.length
        return self.song_genre


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.name
        return self.user
        return self.songs

