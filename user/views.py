from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import User
from django.contrib.auth import get_user_model
from .models import User

from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # User = get_user_model()

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer