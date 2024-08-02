from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:game_id>', views.one_game),
]