from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = get_user_model() # User
        # fields = '__all__'
        fields = ['url', 'id', 'username', 'updated_at', 'password', 'groups']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # user.groups.add(Group.objects.get(name="Admin"))
        # user.groups.add(Group.objects.get(id=2))        
        return user

    def update(self, instance, validated_data):
        instance = super(UserSerializer, self).update(instance, validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance