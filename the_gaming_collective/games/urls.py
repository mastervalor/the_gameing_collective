from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.index),
    path('games_list', views.games),
    path('<int:game_id>/<str:game_name>', views.one_game),
    path('your_games', views.users_games),
    path('view_all/<str:game_type>', views.view_all),
]