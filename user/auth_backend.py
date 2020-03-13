from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class MyBackend(BaseBackend):
    '''
    superuser : test / test123
    '''
    def authenticate(self, request, username=None, password=None):
        User = get_user_model() # or use settings.AUTH_USER_MODEL

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        return user

        # login_valid = ('test' == username)
        # pwd_valid = ('test123' == password)

        # if login_valid and pwd_valid:
        #     try:
        #         user = User.objects.get(username=username)
        #     except User.DoesNotExist:
        #         return None
        #     return user
        # else:
        #     return None

    def get_user(self, user_id):
        User = get_user_model() # or use settings.AUTH_USER_MODEL

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    