from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import (
    index, account_creation, finalize_page, finalize_account,
    login_view, edit_account, update_account, delete_account, logout_view
)


