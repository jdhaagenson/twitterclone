from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=140)


    def __str__(self):
        return f'@{self.author}'
