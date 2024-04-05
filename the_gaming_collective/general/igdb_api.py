from igdb.wrapper import IGDBWrapper
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.views.generic.base import View
import json
import requests

IGDB_CLIENT_ID = "1ucj7p9lz76qmng4s8xpcwoh0h69j5"
IGDB_API_KEY = "5qm7yknzijrnanrgy315m97mmq2esp" #xxt4b3edw4naybndia41x6mztikri5

def validate_api_key(api_key):
    igdb_api_endpoint = "https://api.igdb.com/v4/games"

    headers = {
        "Client-ID": IGDB_CLIENT_ID,
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(igdb_api_endpoint, headers=headers)

    print(response.url)

    if response.status_code == 200:
        return True;
    else:
        return False;

def update_api_key():
    twitch_api_endpoint = "https://id.twitch.tv/oauth2/token"

    params = {
        "client_id": "1ucj7p9lz76qmng4s8xpcwoh0h69j5",
        "client_secret": "5uvqpxec96xxlfb87dba8hs07rvac1",
        "grant_type": "client_credentials"
    }

    response = requests.post(twitch_api_endpoint, params=params)

    if response.status_code == 200:
        response_json = response.json()
        new_api_key = response_json.get('access_token')

        global IGDB_API_KEY
        IGDB_API_KEY = new_api_key

        print(f"API Token updated successfully: {IGDB_API_KEY}")
    else:
        print("Failed to obtain new API Token")

def igdb_token_check():
    if not validate_api_key(IGDB_API_KEY):
        print("Invalid IGDB API Token")
    
        # Attempt to update the API key
        update_api_key()
    
        # Check again if the updated API key is valid
        if not validate_api_key(IGDB_API_KEY):
            raise ValueError("Failed to obtain a valid IGDB API Token")
        else:
            print("API key updated successfully.")
    else:
        print(f"\nAPI Token: {IGDB_API_KEY}")
        print("API key is valid.\n")
        
igdb_token_check()

wrapper = IGDBWrapper(IGDB_CLIENT_ID, IGDB_API_KEY)
print(wrapper)

class igdb_api(View):
    @classmethod
    def get_games_list(cls):

        all_games = []
        developers = [
            "Nintendo", "Square Enix", "Ubisoft Entertainment",
            "Activision", "Activision Blizzard",
            "Bethesda", "Capcom", "Sony Interactive Entertainment",
            "BioWare", "Epic Games", "FromSoftware", "Bungie",
            "2K Games", "Insomniac Games", "Respawn Entertainment",
            "Guerrilla Games", "Respawn Entertainment", "DICE", "2K games",
            "CD Projekt RED", "505 Games", "Konami", "Naughty Dog",
            "Riot Games", "Bandai Namco Games", "Remedy Entertainment",
            "NetherRealm Studios", "HEXWORKS", "Turn 10 Studios", "Polyphony Digital",
            "Obsidian Entertainment", "Larian Studios", "Focus Entertainment",
            "Mundfish", "Devolver Digital", "Colossal Order", "Tripwire Interactive",
            "Ubisoft Bordeaux", "Ubisoft Montreal", "Infinity Ward",
            "Sledgehammer Games", "Geometric Interactive", "Motive Studios", "id Software",
            "Criterion Software", "Luminous Productions",
            "Red Barrels", "Arkane Studios", "Tango Gameworks", "Black Salt Games",
            "Neowiz Games", "Sabotage Studio", "Dambuster Studios", "Relic Entertainment",
            "Team NINJA", "Avalanche Software", "Intelligent Systems", "Omega Force",
            "Behaviour Interactive", "P Studio", "Rundisc", "Mojang Studios",
            "PlatinumGames", "Starbreeze Studios", "Nightdive Studios", "Gunfire Games",
            "Gearbox Software", "Massive Entertainment", "Frictional Games", "WayForward",
            "Night School Studio", "Ascendant Studios", "Teyon", "Rocksteady Studios"
        ]

        # Need to add ^ (u"Eidos-Montr�al", u"WB Games Montr�al",)

        offset = 0
        limit = 500

        where_plat = 'platforms.name = "Xbox Series X|S" | platforms.name = "PlayStation 5" | platforms.name = "Nintendo Switch" | platforms.name = "PC"'
        where_dev = " | ".join([f'involved_companies.company.name = "{name}"' for name in developers])
        if_dev = 'involved_companies.developer = true'
        

        while True:
            response = wrapper.api_request(
                'games',
                f'fields name, cover.image_id, summary, first_release_date, rating, age_ratings, platforms, platforms.name, expansions, game_engines, game_modes, genres.name, multiplayer_modes, player_perspectives, screenshots, websites, involved_companies.company.name, parent_game, version_title, release_dates.human, release_dates.category, videos.name, videos.video_id; offset {offset}; limit {limit}; where ({where_plat}) & ({where_dev}) & ({if_dev});'
            )

            games_batch = json.loads(response)

            if not games_batch:
                break

            all_games.extend(games_batch)

            offset += limit

        return all_games