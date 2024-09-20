from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User 

class TestAccountViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response, 200)
        self.assertTemplateUsed(response, 'ogin_create.htm')