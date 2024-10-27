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
        
    def test_account_creation_invalid_data(self):
        postData = {
            'first_name': 'A',  # Invalid first name (too short)
            'last_name': 'Smith',
            'email': 'invalidemail',  # Invalid email format
            'password': 'password',
            'password_confirm': 'password123'  # Passwords do not match
        }
        response = self.client.post(reverse('account_creation'), postData)
        self.assertRedirects(response, '/account/user/create')
        messages_list = list(response.wsgi_request._messages)
        self.assertGreater(len(messages_list), 0)
    
    def test_login_view_success(self):
        self.user.password = bcrypt.hashpw("password123".encode(), bcrypt.gensalt()).decode()
        self.user.save()
        postData = {'email': self.user.email, 'password': 'password123'}
        response = self.client.post(reverse('login_view'), postData)
        self.assertRedirects(response, '/')
        self.assertEqual(self.client.session['user_id'], self.user.id)
        
    def test_login_view_invalid_password(self):
        postData = {'email': self.user.email, 'password': 'wrongpassword'}
        response = self.client.post(reverse('login_view'), postData)
        self.assertRedirects(response, '/account/login_create/')
        messages_list = list(response.wsgi_request._messages)
        self.assertIn("This password doesn't match", str(messages_list[0]))

    def test_finalize_account(self):
        self.client.session['user_id'] = self.user.id
        postData = {'username': 'newusername', 'devices': [self.device.id]}
        response = self.client.post(reverse('finalize_account'), postData)
        self.assertRedirects(response, '/')
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertIn(self.device, self.user.fav_devices.all())
    
    def test_edit_account_view(self):
        self.client.session['user_id'] = self.user.id
        response = self.client.get(reverse('edit_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_account.html')
        self.assertEqual(response.context['user'], self.user)
    
    def test_delete_account(self):
        self.client.session['user_id'] = self.user.id
        response = self.client.post(reverse('delete_account'))
        self.assertRedirects(response, '/account')
        self.assertFalse(Users.objects.filter(id=self.user.id).exists())
    
    def test_update_account_valid(self):
        self.client.session['user_id'] = self.user.id
        postData = {
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
            'email': 'updated@example.com',
            'username': 'updateduser',
            'devices': [self.device.id]
        }
        response = self.client.post(reverse('update_account'), postData)
        self.assertRedirects(response, '/')
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedFirstName')
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertIn(self.device, self.user.fav_devices.all())
    
    def test_update_account_invalid(self):
        self.client.session['user_id'] = self.user.id
        postData = {
            'first_name': 'A',  # Invalid first name
            'last_name': 'UpdatedLastName',
            'email': 'invalidemail',  # Invalid email format
            'username': 'updateduser'
        }
        response = self.client.post(reverse('update_account'), postData)
        self.assertRedirects(response, '/account/edit_account')
        messages_list = list(response.wsgi_request._messages)
        self.assertGreater(len(messages_list), 0)
        