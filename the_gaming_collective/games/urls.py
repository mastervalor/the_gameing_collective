from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('games_list', views.games),
    path('<int:game_id>', views.one_game),
    path('your_games/<int:user_id>', views.users_games),
    path('view_all_platform/<int:platform_id>', views.view_all_platform),
    path('view_all_genre/<int:genre_id>', views.view_all_genre),
    path('view_all_marketplace/<int:marketplace_id>', views.view_all_marketplace),
    path('<int:game_id>/review', views.review_game),
    path('submit_review/<int:game_id>', views.submit_review),
    path('search_results', views.search),
    path('like/<int:game_id>', views.likes),
]