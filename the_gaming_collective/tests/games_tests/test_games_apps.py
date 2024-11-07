from django.apps import apps
from django.test import SimpleTestCase
from games.apps import GamesConfig

class GamesConfigTest(SimpleTestCase):
    def test_apps(self):
        """Test that the GamesConfig app is correctly configured."""
        self.assertEqual(GamesConfig.name, 'games')
        self.assertEqual(apps.get_app_config('games').name, 'games')