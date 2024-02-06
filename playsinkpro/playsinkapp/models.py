from django.db import models
from django.contrib.auth.models import User

class song_Genre(models.Model):
    name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)


class song_Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    artist_name = models.ForeignKey(song_Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    length = models.DurationField()
    song_genre = models.ForeignKey(song_Genre, on_delete=models.CASCADE)


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
