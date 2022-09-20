from django.db import models
from account.models import Users


class Messages(models.Model):
    message_context = models.TextField()
    sender = models.ForeignKey(Users, blank=True, null=True, related_name = "sender", on_delete = models.CASCADE)
    reciver = models.ForeignKey(Users, blank=True, null=True, related_name= "reciver", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    