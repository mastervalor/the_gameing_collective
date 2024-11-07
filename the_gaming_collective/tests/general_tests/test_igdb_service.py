from django.test import TestCase
from django.core.cache import cache
from unittest.mock import patch
from general.igdb_service import get_games

class GetGamesCacheTest(TestCase):
    def setUp(self):
        cache.clear()
    
    @patch('general.igdb_api.igdb_token_check')
    @patch('general.igdb_api.get_games_in_batches')
    def test_get_games_cached_data(self, mock_get_games_in_batches, mock_igdb_token_check):
        """Test that cached data is returned if it exists and is still valid."""
        # Mock data and expiration
        mock_data = [{"id": 1, "name": "Cached Game"}]
        cache_key = 'games'
        expiration_time_key = 'games_timeout'

        # Set mock cache values
        expiration_time = datetime.now() + timedelta(seconds=1800)
        cache.set(cache_key, mock_data, 1800)
        cache.set(expiration_time_key, expiration_time, 1800)

        result = get_games()

        # Check if cached data is returned and external calls are not made
        self.assertEqual(result, mock_data)
        mock_igdb_token_check.assert_not_called()
        mock_get_games_in_batches.assert_not_called()
    
    @patch('general.igdb_api.igdb_token_check')
    @patch('general.igdb_api.get_games_in_batches')
    def test_get_games_no_cache_data(self, mock_get_games_in_batches, mock_igdb_token_check):
        """Test that data is fetched from IGDB if cache is empty or expired."""
        mock_data = [{"id": 2, "name": "New Game"}]
        mock_get_games_in_batches.return_value = mock_data

        result = get_games()

        # Check if data is fetched, token check is called, and cache is set
        mock_igdb_token_check.assert_called_once()
        mock_get_games_in_batches.assert_called_once()
        self.assertEqual(result, mock_data)
        self.assertEqual(cache.get('games'), mock_data)
        
    @patch('general.igdb_api.igdb_token_check')
    @patch('general.igdb_api.get_games_in_batches')
    def test_get_games_cache_expired(self, mock_get_games_in_batches, mock_igdb_token_check):
        """Test that expired cache triggers a fresh fetch."""
        mock_data = [{"id": 3, "name": "Refreshed Game"}]
        cache_key = 'games'
        expiration_time_key = 'games_timeout'

        # Set expired cache values
        cache.set(cache_key, [{"id": 1, "name": "Old Game"}], 1800)
        expired_time = datetime.now() - timedelta(seconds=10)
        cache.set(expiration_time_key, expired_time, 1800)

        # Update mock return
        mock_get_games_in_batches.return_value = mock_data

        result = get_games()

        # Check that expired data was replaced with new data
        mock_igdb_token_check.assert_called_once()
        mock_get_games_in_batches.assert_called_once()
        self.assertEqual(result, mock_data)
        self.assertEqual(cache.get(cache_key), mock_data)
        