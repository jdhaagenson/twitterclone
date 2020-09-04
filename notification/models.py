from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your models here.
class Notification(models.Model):
    message = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.author
