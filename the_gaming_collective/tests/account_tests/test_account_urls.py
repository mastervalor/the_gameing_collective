from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import (
    index, account_creation, finalize_page, finalize_account,
    login_view, edit_account, update_account, delete_account, logout_view
)

class TestUrls(SimpleTestCase):
    def test_login_create_url_resolves(self):
        url = '/login_create/'
        self.assertEqual(resolve(url).func, index)

    def test_account_creation_url_resolves(self):
        url = '/user/create'
        self.assertEqual(resolve(url).func, account_creation)
    
    def test_finalize_page_url_resolves(self):
        url = '/finalize'
        self.assertEqual(resolve(url).func, finalize_page)
    
    def test_finalize_account_url_resolves(self):
        url = '/process'
        self.assertEqual(resolve(url).func, finalize_account)
    
    def test_login_view_url_resolves(self):
        url = '/user/login'
        self.assertEqual(resolve(url).func, login_view)
    
    def test_edit_account_url_resolves(self):
        url = '/account/'
        self.assertEqual(resolve(url).func, edit_account)
        