from django.core.cache import cache
from general.igdb_api import igdb_api  # Import your IGDB API client

CACHE_TIMEOUT = 7200  # Set your cache timeout in seconds

def get_aaa_upcoming_games():
    cache_key = 'aaa_upcoming_games'

    # Attempt to retrieve data from the cache
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    # If data is not cached, fetch it from IGDB
    all_games = igdb_api.get_aaa_upcoming_games()

    # Store the fetched data in the cache
    cache.set(cache_key, all_games, CACHE_TIMEOUT)

    return all_games