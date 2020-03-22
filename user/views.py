from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import User

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    # User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer