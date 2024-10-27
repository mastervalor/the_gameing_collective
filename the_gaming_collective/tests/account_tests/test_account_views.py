from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import Users, Devices


class TestAccountViews(TestCase):
    def setUp(self):
        # Set up a test user and a device
        self.user = Users.objects.create(
            email="testuser@example.com",
            password="hashed_password",
            first_name="Test",
            last_name="User",
            username="testuser"
        )
        self.device = Devices.objects.create(device="Laptop", dev_id=123)
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response, 200)
        self.assertTemplateUsed(response, 'ogin_create.htm')
        
    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout_view'))
        self.assertRedirects(response, '/')
    
    def test_account_creation_valid_data(self):
        postData = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'alice@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!'
        }
        response = self.client.post(reverse('account_creation'), postData)
        self.assertRedirects(response, '/account/finalize')
        self.assertTrue(Users.objects.filter(email='alice@example.com').exists())
        