from django.db import models
from account.models import Users

class Games(models.Model):
    game_id = models.IntegerField()
    genre = models.CharField(max_length=45)
    fav_games = models.ManyToManyField(Users, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Reviews(models.Model):
    review = models.TextField()
    score = models.DecimalField(max_digits=2, decimal_places=1)
    reviewer = models.ForeignKey(Users, blank=True, null=True, on_delete = models.CASCADE)
    game = models.ForeignKey(Games, blank=True, null=True, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

