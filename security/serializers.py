from rest_framework import serializers

from .models import User, Data

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class  DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'title', 'file']
        read_only = ['id']
