from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from games.views import get_upcoming_games, get_recent_releases, get_one_game
import datetime