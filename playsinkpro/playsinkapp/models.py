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
    


class Song_Artist(models.Model):
    artist_name = models.CharField(max_length=100, verbose_name="Artist")
    song_name = models.CharField(max_length=100, verbose_name="Song")
    category = models.CharField(max_length=100, verbose_name="Category")

    def __str__(self):
        return f"{self.artist_name} - {self.song_name}"


class Song(models.Model):
    CAT = ((1,"Romantic"),(2,"Motivational"),(3,"Sad"),(4,"energetic"),(5,"pop"))

    song_title = models.CharField(max_length=100,verbose_name = "title")
    artist_name = models.ForeignKey(Song_Artist, verbose_name = "artist",on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100,verbose_name = "album")
    length = models.DurationField(verbose_name = "Duration")
    song_genre = models.ForeignKey(song_Genre,verbose_name = "Genre", on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to="image")
    song_file = models.FileField(upload_to="songs")

    def __str__(self):
        return self.song_title
        return self.artist_name
        return self.album_name
        return self.length
        return self.song_genre


class User_Playlist(models.Model):
    user = models.ForeignKey(User,verbose_name = "user_name" ,on_delete=models.CASCADE)
    songs = models.ForeignKey(Song,verbose_name = "songs_name", on_delete=models.CASCADE,blank = True)
def __str__(self):
    return f"{self.user.username}'s Playlist: {self.songs.song_title}"
