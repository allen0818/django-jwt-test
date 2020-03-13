from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from django.contrib.auth import get_user_model
from django.db import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model() # User
        fields = '__all__'
        # fields = ('name', 'password')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        token['name'] = 'extra_info' # not working
        return token