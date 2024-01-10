from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_friends),
    path('add_friend', views.add_friend)
]