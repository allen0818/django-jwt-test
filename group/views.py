from rest_framework import viewsets, permissions
from django.contrib.auth.models import Group
from .serializers import GroupSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]