# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User

from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer