from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.db.models import Q
from .models import Song_Artist, User_Playlist
from .models import song_Genre
from .models import Song


def home(request):
    songs = Song.objects.all() 
    songs = Song.objects.order_by('song_title')

    return render(request, 'index.html', {'songs': songs})
def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        context = {}
        if uname == "" or upass == "":
            context['errormsg'] = "Please fill in all fields."
            return render(request, 'login.html',context)
        else:
            u = authenticate(username = uname, password =upass)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errormsg']="invalid username or password"
                return render(request, 'login.html',context)
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/home')

def playlist(request):
    return render(request, 'playlist.html')
def cooki(request):
    return render(request, 'cookie.html')
def lgl(request):
    return render(request, 'lgl.html')
def privacy(request):
    return render(request, 'pvc.html')


def artist(request):
    artists = Song_Artist.objects.order_by('artist_name')
    context = {'artists': artists}
    return render(request, 'artist.html', {'artists': artists})


def genre_songs(request):
    genres = song_Genre.objects.all()
    return render(request, 'genre.html', {'genres': genres})



def register(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        ucpass = request.POST.get('ucpass')
        
        if uname == "" or upass == "" or ucpass == "":
            errormsg = "Please fill in all fields."
            return render(request, 'register.html', {'errormsg': errormsg})
        elif upass != ucpass:
            errormsg = "Password and confirm password do not match."
            return render(request, 'register.html', {'errormsg': errormsg})
        else:
            try:
                User.objects.create_user(username=uname, password=upass)
                success = "User registered successfully."
                return render(request, 'register.html', {'success': success})
            except IntegrityError:
                errormsg = "Username already exists."
                return render(request, 'register.html', {'errormsg': errormsg})
    else:
        return render(request, 'register.html')
def add_to_playlist(request, song_id):
    if request.method == 'GET':
        song = Song.objects.get(pk=song_id)
        user = request.user
        playlist_songs = user.user_playlist_set.all()
        if playlist_songs.filter(songs=song).exists():
            msg = "Song already exists in your playlist."
        else:
            User_Playlist.objects.create(user=user, songs=song)
            msg = "Song added to your playlist successfully."
        return render(request, 'playlist.html', {'msg': msg})
    else:
        return redirect('/login')
def remove_from_playlist(request, song_id):
    if request.method == 'GET':
        user = request.user
        try:
            playlist_song = User_Playlist.objects.get(user=user, songs_id=song_id)
            playlist_song.delete()
            msg = "Song removed from your playlist successfully."
        except User_Playlist.DoesNotExist:
            msg = "Song does not exist in your playlist."
        return redirect('/playlist', {'msg': msg})
    else:
        return redirect('/login')
def search_song(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        if search_term:
            searched_songs = Song.objects.filter(song_title__icontains=search_term)
            return render(request, 'search_results.html', {'searched_songs': searched_songs, 'search_term': search_term})
        else:
            return render(request, 'search_results.html', {'error_message': 'Please enter a search term.'})
    else:
        return render(request, 'search_results.html', {'error_message': 'Invalid request method.'})

def create_playlist(request):
    if request.method == 'POST':
        playlist_name = request.POST.get('playlist_name')
        if playlist_name:
            # Create a new playlist for the current user
            user = request.user
            playlist = User_Playlist.objects.create(user=user, name=playlist_name)
            # Redirect the user to the home page (index.html) or any other page as needed
            return redirect('/home')  # Change the URL as needed
    return render(request, 'create_playlist.html')