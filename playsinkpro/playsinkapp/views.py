from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def home (request):
    return render(request, 'index.html',)
def login (request):
    return render(request, 'login.html',)
def logout (request):
    return render(request, 'logout.html',)
def playlist (request):
    return render(request, 'playlist.html',)
def search (request):
    return render(request, 'search.html',)
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
            # Create a new user object and save it
            User.objects.create_user(username=uname, password=upass)
            success = "User registered successfully."
            return render(request, 'register.html', {'success': success})
    else:
        # GET request, render the registration form
        return render(request, 'register.html')