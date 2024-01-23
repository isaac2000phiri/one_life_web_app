from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','phone', 'email', 'province', 'date', 'is_active')

