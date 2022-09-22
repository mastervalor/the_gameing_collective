from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.account_creation),
    path('finalize', views.finalize_page),
    path('process', views.finalize_account),
    path('user/login', views.login)
]