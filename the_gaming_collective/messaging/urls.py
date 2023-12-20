from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chat_list, name='messages'),
    path('chats/<int:chat_id>', views.chat_detail)
]