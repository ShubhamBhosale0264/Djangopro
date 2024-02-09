from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

def home(request):
    return render(request, 'index.html')

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

def logout(request):
    return render(request, 'logout.html')

def playlist(request):
    return render(request, 'playlist.html')

def search(request):
    return render(request, 'search.html')

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
