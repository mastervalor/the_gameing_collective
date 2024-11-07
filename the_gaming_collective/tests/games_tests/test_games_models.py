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
        
    def test_create_review(self):
        """Test that a review can be created with valid fields."""
        review = Reviews.objects.create(
            review="Great game!",
            score=8.5,
            reviewer=self.user,
            game_api_id=101
        )
        self.assertEqual(review.review, "Great game!")
        self.assertEqual(review.score, 8.5)
        self.assertEqual(review.reviewer, self.user)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        
    def test_review_score_constraints(self):
        """Test that the review score respects max_digits and decimal_places."""
        with self.assertRaises(Exception):
            Reviews.objects.create(review="Invalid score", score=100.5, reviewer=self.user, game_api_id=101)
        with self.assertRaises(Exception):
            Reviews.objects.create(review="Invalid score", score=8.55, reviewer=self.user, game_api_id=101)
