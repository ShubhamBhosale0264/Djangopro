from django.urls import path
from playsinkapp import views

urlpatterns = [
    path('home',views.home),
]