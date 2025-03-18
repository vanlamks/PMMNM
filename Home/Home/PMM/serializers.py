from rest_framework import serializers
from .models import Restaurant, User

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_number', 'full_name', 'email', 'password_hash', 'created_at']