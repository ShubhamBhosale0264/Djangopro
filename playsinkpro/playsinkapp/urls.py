from django.urls import path
from playsinkapp import views

urlpatterns = [
    path('home',views.home),
    path('login',views.login),
    path('logout',views.logout),
    path('register',views.register),

]