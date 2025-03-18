from rest_framework import serializers
from .models import Restaurant, Menus

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'  

class MenuSerializer(serializers.ModelSerializer):
    restaurant_number = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),  # Lấy dữ liệu từ bảng Restaurant
        source="restaurant",  # Gán vào trường restaurant của model Menu
        write_only=True  
    )
    restaurant = RestaurantSerializer(read_only=True)  # Trả về thông tin nhà hàng đầy đủ

    class Meta:
        model = Menus
        fields = ['menu_number', 'menu_name', 'price', 'description', 'image_url', 'restaurant', 'restaurant_number']


