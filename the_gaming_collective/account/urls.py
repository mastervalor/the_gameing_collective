from django.urls import path
from . import views

urlpatterns = [
    path('login_create', views.index),
    path('user/create', views.account_creation),
    path('finalize', views.finalize_page),
    path('process', views.finalize_account),
    path('user/login', views.login),
    path('account', views.edit_account),
    path("edit_account", views.update_account),
    path('delete_account', views.delete_account),
    path('logout', views.logout),
]