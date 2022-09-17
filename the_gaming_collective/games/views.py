from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from datetime import datetime
import json

# Create your views here.


def index(request):
    
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    # Upcoming PS5 and Xbox Series X|S games (Can be expanded to PC just needs to be worked)
    up_json = igdb_api.api_get_upcoming_games(milliseconds)
    up_games = json.loads(up_json)

    #Game pass games
    gp_json = igdb_api.api_get_game_pass_games()
    gp_games = json.loads(gp_json)
    
    return render(request, "homepage.html", {'gp_list': gp_games, 'up_list': up_games})

def games(request):

    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    # Games by console

    #PS5 games
    ps5_json = igdb_api.api_get_games_by_platform(167, milliseconds)
    ps5_games = json.loads(ps5_json)

    #Xbox series X|S games
    xbox_xs_json = igdb_api.api_get_games_by_platform(169, milliseconds)
    xbox_xs_games = json.loads(xbox_xs_json)

    #PC games
    pc_json = igdb_api.api_get_games_by_platform(6, milliseconds)
    pc_games = json.loads(pc_json)

    # doing genre pulls this way because if I try to pull all games there are too many
    # and I'm unable to get a decent list even out of 500 results

    #Adventure games
    adv_json = igdb_api.api_get_games_by_genre(31, milliseconds)
    adv_games = json.loads(adv_json)

    #FPS/TPS games
    fps_json = igdb_api.api_get_games_by_genre(5, milliseconds)
    fps_games = json.loads(fps_json)

    #Fighting games
    fight_json = igdb_api.api_get_games_by_genre(4, milliseconds)
    fight_games = json.loads(fight_json)

    #Racing games
    race_json = igdb_api.api_get_games_by_genre(10, milliseconds)
    race_games = json.loads(race_json)

    #Sport games
    sport_json = igdb_api.api_get_games_by_genre(14, milliseconds)
    sport_games = json.loads(sport_json)
    return render(request, "games_page.html", {'adv_list': adv_games,
    'fps_list': fps_games, 'fight_list': fight_games, 'race_list': race_games, 'sport_list': sport_games,
    'ps5_list': ps5_games, 'xbox_xs_list': xbox_xs_games, 'pc_list': pc_games})

def one_game(request, game_id):
    game_json = igdb_api.api_get_one_game(game_id)
    game = json.loads(game_json)
    return render(request, "one_game.html", {'one_game': game})

def users_games(request):
    return render(request, "users_games.hmtl")

def view_all(request):
    return render(request, "view_all.html")

def review_game(request, game_id):
    game_json = igdb_api.api_get_one_game(game_id)
    game = json.loads(game_json)
    return render(request, "review_page.html", {'one_game': game})

def submit_review(request, game_id):
    return redirect(f"/games/{game_id}")