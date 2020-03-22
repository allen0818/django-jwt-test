from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims into token
        token['name'] = user.username
        return token

    # ref: https://stackoverflow.com/questions/53480770
    # def validate(self, attrs):
    #     data = super(MyTokenObtainPairSerializer, self).validate(attrs)
    #     data.update({'name': self.user.username})
    #     data.update({'info': 'some extra infos'})
    #     return data