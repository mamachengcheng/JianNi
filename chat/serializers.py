# **coding: utf-8**
from rest_framework import serializers
from chat.models import Friend, User
from time import strftime


class FriendListSerializer(serializers.ModelSerializer):

    friend_name = serializers.SerializerMethodField()
    last_time = serializers.SerializerMethodField()

    class Meta:
        model = Friend
        fields = ('id', 'friend_name', 'last_time', 'last_message')

    def get_friend_name(self, obj):
        return User.objects.get(id=obj.friend_id).username

    def get_last_time(self, obj):
        return obj.last_time.strftime("%H:%M")


