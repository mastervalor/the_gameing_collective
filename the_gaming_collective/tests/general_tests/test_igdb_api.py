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