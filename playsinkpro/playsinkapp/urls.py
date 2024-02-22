from django.urls import path
from playsinkapp import views

urlpatterns = [
    path('home',views.home),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('playlist',views.playlist),
    path('artist',views.artist),
    path('about',views.about),



]