from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    role = models.CharField(max_length=20)
    health = models.IntegerField(default=100)

    def __str__(self):
        return f"Player {self.pk}"


class Games(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=1)
    game_name = models.CharField(max_length=50)
    health = models.IntegerField(default=100)


    def __str__(self):
        return f"Game #{self.pk}"


class ChatText(models.Model):
    answer_player = models.TextField(default='что то я не хочу отвечать ')
    text = models.TextField()
    games = models.ForeignKey(Games, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Chat Text #{self.pk}"





