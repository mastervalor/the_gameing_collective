from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from games.views import get_upcoming_games, get_recent_releases, get_one_game
import datetime

class TestGamesViews(TestCase):
    @patch('games.views.get_games')
    def test_index_view(self, mock_get_games):
        """Test the index view for rendering the homepage with games data."""
        # Mock data
        mock_data = [
            {"id": 1, "name": "Upcoming Game", "first_release_date": int((datetime.datetime.now() + datetime.timedelta(days=10)).timestamp())},
            {"id": 2, "name": "Recent Game", "first_release_date": int((datetime.datetime.now() - datetime.timedelta(days=30)).timestamp())},
        ]
        mock_get_games.return_value = mock_data

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage.html")
        self.assertIn("upcoming_games", response.context)
        self.assertIn("recently_released_games", response.context)
        self.assertEqual(len(response.context["upcoming_games"]), 1)
        self.assertEqual(len(response.context["recently_released_games"]), 1)
        