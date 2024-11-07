from django.test import SimpleTestCase
from django.urls import resolve
from games.views import index, one_game

class TestGamesUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        """Test that the root URL ('/') maps to the index view."""
        url = '/'
        self.assertEqual(resolve(url).func, index)
