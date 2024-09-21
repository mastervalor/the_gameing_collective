from django.test import TestCase
from account.models import UserManager, Users, Devices

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
        self.assertEqual(errors, {})
        
    def test_finalize_invalid_usernam(self):
        postData = {
        'devices': ['Xbox'],
        'username': 'j'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
    
    def test_finalize_no_devices(self):
        postData = {
        'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_finalize_duplicate_username(self):
        postData = {
            'devices': ['Xbox'],
            'username': 'johndoe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
         

class DevicesModelTest(TestCase):
    def test_create_device(self):
        device = Devices.objects.create(device="Smartphone", dev_id=101)
        self.assertEqual(device.device, "Smartphone")
        self.assertEqual(device.dev_id, 101)
    
    def test_device_max_length(self):
        device = Devices.objects.create(device="a" * 45, dev_id=102)
        self.assertEqual(device.device, "a" * 45)
        
    def test_invalid_device_max_lenth(self):
        with self.assertRaises(Exception):
            Devices.objects.create(device="a" * 46, dev_id=103) 
    
    def test_invalid_device_max_length(self):
        with self.assertRaises(Exception):
            Devices.objects.create(device="Tablet")