from django.test import TestCase
from django.core.cache import cache
from unittest.mock import patch
from general.igdb_service import get_games

class GetGamesCacheTest(TestCase):
    def setUp(self):
        cache.clear() 