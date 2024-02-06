from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)


class Song(models.Model):
    song_title = models.CharField(max_length=100)
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    length = models.DurationField()
    song_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
