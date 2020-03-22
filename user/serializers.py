from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model() # User
        # fields = '__all__'
        fields = ['url', 'id', 'username', 'updated_at']