# Djangorestframework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User general purpose serializer
    """
    class Meta:
        model = User
        fields = ['id', 'username']
