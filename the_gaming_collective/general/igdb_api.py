from igdb.wrapper import IGDBWrapper
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.views.generic.base import View
import json

IGDB_CLIENT_ID = "1ucj7p9lz76qmng4s8xpcwoh0h69j5"
IGDB_API_KEY = "2a3tw9lp0do3bvky8wnbx44hst8omz"

wrapper = IGDBWrapper(IGDB_CLIENT_ID, IGDB_API_KEY)

class igdb_api(View):
    @classmethod
    def get_aaa_upcoming_games(cls):

        all_games = []
        top_aaa = [
            "Nintendo", "Square Enix", "Ubisoft",
            "Activision", "Activision Blizzard",
            "Bethesda", "Capcom", "Sony Interactive Entertainment",
            "BioWare", "Epic Games", "FromSoftware", "Bungie",
            "2K Games", "Insomniac Games", "Respawn Entertainment",
            "Guerrilla Games", "Respawn Entertainment", "DICE", "2K games",
            "CD Projekt RED", "505 Games", "Konami", "Naughty Dog",
            "Riot Games", "Bandai Namco Games"
        ]

        offset = 0
        limit = 500

        where_plat = 'platforms.name = "Xbox Series X|S" | platforms.name = "PlayStation 5" | platforms.name = "Nintendo Switch" | platforms.name = "PC"'
        where_dev = " | ".join([f'involved_companies.company.name = "{name}"' for name in top_aaa])
        if_dev = 'involved_companies.developer = true'
        

        while True:
            response = wrapper.api_request(
                'games',
                f'fields name, cover.image_id, summary, first_release_date, rating, age_ratings, platforms, platforms.name, expansions, game_engines, game_modes, genres, multiplayer_modes, player_perspectives, screenshots, websites, involved_companies.company.name, parent_game, version_title; offset {offset}; limit {limit}; where ({where_plat}) & ({where_dev}) & ({if_dev});'
            )

            games_batch = json.loads(response)

            if not games_batch:
                break

            all_games.extend(games_batch)

            offset += limit

        return all_games