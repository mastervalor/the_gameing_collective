from django.test import TestCase
from account.models import UserManager

class TestAccountModelsUserManager(TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_valid_user_data(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertEqual(errors, {})