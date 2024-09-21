from django.test import TestCase
from account.models import UserManager, Users

class TestAccountModelsUserManager(TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.existing_user = Users.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            username='johndoe',
            password='hashed_password'
        )

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
        
    def test_invalid_email(self):
        postData = {
            'email': 'invalid.email',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_short_first_name(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_passwords_do_not_match(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPaword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_short_password(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'Valid!',
            'password_confirm': 'Valid!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_vaild_edit_data(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertEqual(errors, {})
        
    def test_invalid_edit_email(self):
        postData = {
            'email': 'invalid.email',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_short_first_name(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_no_device(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_duplicate_username(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'johndoe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_short_username(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'j'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_finalize_valid_user_validator(self):
        postData = {
        'devices': ['Xbox'],
        'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        