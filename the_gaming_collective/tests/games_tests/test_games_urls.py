from django.test import SimpleTestCase
from django.urls import resolve
from games.views import index, one_game

class TestGamesUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        """Test that the root URL ('/') maps to the index view."""
        url = '/'
        self.assertEqual(resolve(url).func, index)

    def test_one_game_url_resolves(self):
        """Test that '/<int:game_id>' maps to the one_game view."""
        url = '/1'  # Example of a valid URL with game_id as 1
        resolved = resolve(url)
        self.assertEqual(resolved.func, one_game)
        self.assertEqual(resolved.kwargs['game_id'], 1)
        