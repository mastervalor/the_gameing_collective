from django.db import models

class Users(models.Model):
    email = models.EmailField('User Email')
    password = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    friend_id = models.ManyToManyField("self")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Platforms(models.Model):
    platform = models.CharField(max_length=45)
    fav_platforms = models.ManyToManyField(Users, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Devices(models.Model):
    device = models.CharField(max_length=45)
    fav_devices = models.ManyToManyField(Users, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)