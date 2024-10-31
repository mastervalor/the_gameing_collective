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
    
    def test_get_upcoming_games(self):
        """Test filtering games with future release dates in get_upcoming_games."""
        today = datetime.datetime.now().date()
        future_date = int((datetime.datetime.now() + datetime.timedelta(days=10)).timestamp())
        past_date = int((datetime.datetime.now() - datetime.timedelta(days=30)).timestamp())

        game_data = [
            {"id": 1, "name": "Future Game", "first_release_date": future_date, "parent_game": None, "version_title": None},
            {"id": 2, "name": "Past Game", "first_release_date": past_date, "parent_game": None, "version_title": None},
        ]

        upcoming_games = get_upcoming_games(game_data)
        self.assertEqual(len(upcoming_games), 1)
        self.assertEqual(upcoming_games[0]["name"], "Future Game")
        
    def test_get_recent_releases(self):
        """Test filtering games released in the past 90 days in get_recent_releases."""
        today = datetime.datetime.now().date()
        recent_date = int((datetime.datetime.now() - datetime.timedelta(days=30)).timestamp())
        old_date = int((datetime.datetime.now() - datetime.timedelta(days=100)).timestamp())

        game_data = [
            {"id": 1, "name": "Recent Game", "first_release_date": recent_date, "parent_game": None, "version_title": None},
            {"id": 2, "name": "Old Game", "first_release_date": old_date, "parent_game": None, "version_title": None},
        ]

        recently_released_games = get_recent_releases(game_data)
        self.assertEqual(len(recently_released_games), 1)
        self.assertEqual(recently_released_games[0]["name"], "Recent Game")
        
    