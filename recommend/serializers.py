# **coding: utf-8**
from rest_framework import serializers
from chat.models import User


class IndexCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'location', 'rank')
