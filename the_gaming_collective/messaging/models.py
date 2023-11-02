from django.db import models
from account.models import Users

class Chat(models.Model):
    participants = models.ManyToManyField(Users, related_name='chats')
    last_message = models.DateTimeField(null=True)
  
class Message(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  sender = models.ForeignKey(Users, related_name='messages_sent', on_delete = models.CASCADE)
  receiver = models.ForeignKey(Users, related_name='messages_received', on_delete = models.CASCADE) 
  message_content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)