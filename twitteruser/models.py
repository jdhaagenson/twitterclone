from django.db import models
from django.contrib.auth.models import AbstractUser
from tweet.models import Tweet


# Create your models here.
class TwitterUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, default=None)

    def __str__(self):
        return self.username
