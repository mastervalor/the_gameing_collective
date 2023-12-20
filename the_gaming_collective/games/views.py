from django.shortcuts import render
from general.igdb_api import igdb_api
from general.igdb_service import get_games
import json, datetime
from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
def index(request):
    all_games = get_games()
    
    upcoming_games = get_upcoming_games(all_games)
    recently_released_games = get_recent_releases(all_games)

    return render(request, "homepage.html", {'upcoming_games': upcoming_games, 'recently_released_games': recently_released_games})

# Get Games with a release date that is after 'Today'
def get_upcoming_games(game_results):
    upcoming_games = []

    today = datetime.datetime.now().date()

    for game in game_results:
        # The IGDB only uses UNIX timestamps
        unix_timestamp = game.get('first_release_date')

        # This checks if in the JSON for the game that the first release date was not empty
        if unix_timestamp is not None:
            timestamp_datetime = datetime.datetime.fromtimestamp(unix_timestamp)

            # This checks if the now converted timestamp_datetime is in the future from today's datetime
            if timestamp_datetime.date() > today and game.get('parent_game') == None and game.get('version_title') == None:
                upcoming_games.append(game)
                print(game.get('name'), game.get('first_release_date'), game.get('platforms.name'))

    return upcoming_games

def get_recent_releases(game_results):
    recently_released_games = []

    today = datetime.datetime.now().date()

    delta = datetime.timedelta(days=365)

    date_60_days_ago = today - delta

    for game in game_results:
        unix_timestamp = game.get('first_release_date')

        if unix_timestamp is not None:
            timestamp_datetime = datetime.datetime.fromtimestamp(unix_timestamp)

            if timestamp_datetime.date() < today and timestamp_datetime.date() > date_60_days_ago and game.get('parent_game') == None and game.get('version_title') == None:
               recently_released_games.append(game)
               print(game.get('name'), game.get('id'), game.get('version_title'), game.get('first_release_date'), game.get('platforms.name'))

    return recently_released_games