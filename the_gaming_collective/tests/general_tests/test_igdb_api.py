from django.test import TestCase
from unittest.mock import patch
from general.igdb_service import validate_api_key, update_api_key
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
        
        