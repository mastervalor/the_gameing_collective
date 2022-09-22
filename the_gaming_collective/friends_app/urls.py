from django.urls import path
from . import views

urlpatterns = [
    path('friends', views.index),
]