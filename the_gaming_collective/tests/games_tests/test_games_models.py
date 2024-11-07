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

    def test_review_deletion(self):
        """Test that deleting a review does not affect the user."""
        review = Reviews.objects.create(review="Great game!", score=8.5, reviewer=self.user, game_api_id=101)
        review_id = review.id
        review.delete()
        self.assertFalse(Reviews.objects.filter(id=review_id).exists())
        self.assertTrue(Users.objects.filter(id=self.user.id).exists())

class GamesModelTest(TestCase):
    def setUp(self):
        # Set up a test user and review
        self.user = Users.objects.create(
            email="gamer@example.com",
            password="hashed_password",
            first_name="Alice",
            last_name="Smith",
            username="gamer"
        )
        self.review = Reviews.objects.create(
            review="Amazing RPG!",
            score=9.0,
            reviewer=self.user,
            game_api_id=102
        )
    
    def test_create_game(self):
        """Test that a game can be created with valid fields and relationships."""
        game = Games.objects.create(
            game_api_id=103,
            genre="RPG",
            review=self.review
        )
        self.assertEqual(game.game_api_id, 103)
        self.assertEqual(game.genre, "RPG")
        self.assertEqual(game.review, self.review)
        self.assertIsNotNone(game.created_at)
        self.assertIsNotNone(game.updated_at)
    
    def test_fav_games_relationship(self):
        """Test the ManyToMany relationship for favorite games."""
        game = Games.objects.create(game_api_id=104, genre="Action")
        game.fav_games.add(self.user)
        self.assertIn(self.user, game.fav_games.all())
        self.assertIn(game, self.user.favorite_games.all())
        
    def test_review_deletion_with_game(self):
        """Test that deleting a review also deletes it from the associated game."""
        game = Games.objects.create(game_api_id=105, genre="Adventure", review=self.review)
        self.review.delete()
        game.refresh_from_db()
        self.assertIsNone(game.review)
        