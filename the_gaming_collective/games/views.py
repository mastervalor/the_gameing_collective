from django.shortcuts import render
from general.igdb_api import igdb_api
from datetime import datetime
import json

# Create your views here.


def index(request):
    
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    up_json = igdb_api.api_get_upcoming_games(milliseconds)
    up_games = json.loads(up_json)

    gp_json = igdb_api.api_get_game_pass_games()
    gp_games = json.loads(gp_json)

    adv_json = igdb_api.api_get_games_by_genre(31)
    adv_games = json.loads(adv_json)
    
    return render(request, "homepage.html", {'gp_list': gp_games, 'up_list': up_games, 'adv_list': adv_games
    })