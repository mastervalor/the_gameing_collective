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