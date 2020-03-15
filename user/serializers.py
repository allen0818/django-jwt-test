from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model() # User
        # fields = '__all__'
        fields = [
            'url', 'id', 'username', 'email', 'date_joined', 'phone', 
            'created_at', 'updated_at'
        ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # add custom claims
    #     token['name'] = 'extra_info' # not working
    #     return token

    # ref: https://stackoverflow.com/questions/53480770
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'name': self.user.username})
        data.update({'info': 'some extra infos'})
        return data