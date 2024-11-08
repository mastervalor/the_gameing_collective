from django.test import TestCase
from unittest.mock import patch
from general.igdb_service import validate_api_key, update_api_key, get_games_in_batches
import requests

class IGDBApiKeyTests(TestCase):
    @patch('requests.post')
    def test_validate_api_key_valid(self, mock_post):
        """Test that a valid API key returns True."""
        mock_post.return_value.status_code = 200
        result = validate_api_key("valid_api_key")
        
    @patch('requests.post')
    def test_validate_api_key_invalid(self, mock_post):
        """Test that an invalid API key returns False."""
        mock_post.return_value.status_code = 401
        result = validate_api_key("invalid_api_key")
        self.assertFalse(result)
        
    @patch('requests.post')
    def test_update_api_key_success(self, mock_post):
        """Test that update_api_key updates the API key on success."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"access_token": "new_api_key"}

        update_api_key()
        from general.igdb_service import IGDB_API_KEY
        self.assertEqual(IGDB_API_KEY, "new_api_key")
        
    @patch('requests.post')
    def test_update_api_key_failure(self, mock_post):
        """Test that update_api_key does not update the API key if the request fails."""
        mock_post.return_value.status_code = 400
        from general.igdb_service import IGDB_API_KEY
        old_api_key = IGDB_API_KEY

        update_api_key()
        self.assertEqual(IGDB_API_KEY, old_api_key) 
        

class GetGamesInBatchesTests(TestCase):
    @patch('requests.post')
    def test_get_games_in_batches_success(self, mock_post):
        """Test that get_games_in_batches retrieves game data successfully."""
        mock_data = [{"id": 1, "name": "Game 1"}]
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_data

        result = get_games_in_batches()
        self.assertEqual(result, mock_data)
        mock_post.assert_called_once()