from django.apps import apps
from django.test import SimpleTestCase
from general.apps import GeneralConfig

class GeneralConfigTest(SimpleTestCase):
    def test_apps(self):
        """Test that the GeneralConfig app is configured correctly."""
        self.assertEqual(GeneralConfig.name, 'general')
        self.assertEqual(apps.get_app_config('general').name, 'general')
        