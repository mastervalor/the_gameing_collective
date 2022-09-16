from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.account_creation),
    path('finalize', views.finalize),
    path('testing', views.test),
]