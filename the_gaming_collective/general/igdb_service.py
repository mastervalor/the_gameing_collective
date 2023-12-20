from django.core.cache import cache
from general.igdb_api import igdb_api, igdb_token_check  # Import your IGDB API client
from datetime import datetime, timedelta

CACHE_TIMEOUT = 1800  # Set your cache timeout in seconds

def get_games():
    cache_key = 'games'
    expiration_time_key = cache_key + '_timeout'

    # Attempt to retrieve data from the cache
    cached_data = cache.get(cache_key)
    expiration_time = cache.get(expiration_time_key)

    if cached_data is not None:
        
        current_time = datetime.now()
        
        # Ensure expiration_time is a datetime object
        if isinstance(expiration_time, datetime):
            # Calculate the time remaining in cache
            time_remaining = expiration_time - current_time
            print(f"Time remaining in cache: {time_remaining}")

            # Check if the cached data is still valid
            if current_time < expiration_time:
                return cached_data

    igdb_token_check()

    # If data is not cached, fetch it from IGDB
    all_games = igdb_api.get_games()

    # Store the fetched data in the cache
    cache.set(cache_key, all_games, CACHE_TIMEOUT)

     # Store the expiration time
    expiration_time = datetime.now() + timedelta(seconds=CACHE_TIMEOUT)
    cache.set(expiration_time_key, expiration_time, CACHE_TIMEOUT)

    return all_games