from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

class UserManager(models.Manager):
    def default_user_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['login'] = "That is not a valid email"
        if not PASSWORD_REGEX.match(postData['password']):
            errors['login'] = "Password must have at least eight characters, at least one uppercase letter, one lowercase letter, one number and one special character"
        if len(postData['first_name']) < 2:
            errors['login'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['login'] = 'Last Name must be atleast 2 characters'
        if postData['password_confirm'] != postData['password']:
            errors['login'] = "Your passwords don't match"
        return errors
    
    def edit_user_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['login'] = "That is not a valid email"
        if len(postData['first_name']) < 2:
            errors['login'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['login'] = 'Last Name must be atleast 2 characters'
        if len(postData['devices']) == 0:
            errors['devices'] = "Please pick your favorite Devices"
        if len(postData['username']) < 2:
            errors['username'] = "Username must be longer then 2 letters"
        if postData['username'] == Users.objects.filter(username=f"{postData['username']}"):
            errors['username_match'] = "That username already excits"
        return errors
            
    def finalize_user_validator(self, postData):
        errors = {}
        if len(postData['devices']) == 0:
            errors['devices'] = "Please pick your favorite Devices"
        if len(postData['username']) < 2:
            errors['username'] = "Username must be longer then 2 letters"
        if postData['username'] == Users.objects.filter(username=f"{postData['username']}"):
            errors['username_match'] = "That username already excits"
        return errors
    
class Devices(models.Model):
    device = models.CharField(max_length=45)
    dev_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Users(models.Model):
    email = models.EmailField('User Email')
    password = models.CharField(max_length=60)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, blank=True)
    fav_devices = models.ManyToManyField(Devices, blank=True)
    friend_id = models.ManyToManyField("self")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
