from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    phone = models.CharField(max_length=11)
    username = models.CharField(max_length=15)
    location = models.FloatField()
    weibo_name = models.CharField(max_length=16)
    rank = models.IntegerField()


class Friend(models.Model):
    User = models.ForeignKey(User, related_name='user_friend')
    friend_id = models.IntegerField()
    last_time = models.DateTimeField(auto_now=True)
    last_message = models.TextField()
