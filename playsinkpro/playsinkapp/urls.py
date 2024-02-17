from django.urls import path
from playsinkapp import views

urlpatterns = [
    path('home',views.home),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('playlist',views.playlist),
    path('search',views.search),
    path('about',views.about),
    path('catfilter/<cv>',views.songfilter),


]