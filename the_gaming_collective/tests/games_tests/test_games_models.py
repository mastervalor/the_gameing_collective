from django.test import TestCase
from account.models import Users
from games.models import Reviews, Games

class ReviewsModelTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = Users.objects.create(
            email="reviewer@example.com",
            password="hashed_password",
            first_name="John",
            last_name="Doe",
            username="reviewer"
        )