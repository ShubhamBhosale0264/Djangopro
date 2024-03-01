from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.db.models import Q
# from spotipy.oauth2 import SpotifyClientCredentials
from .models import Song_Artist
from .models import song_Genre
from .models import Song


def home(request):
    songs = Song.objects.all() 
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
