from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Restaurant, Menus  # Import đúng cách
from .serializers import RestaurantSerializer, MenuSerializer

# Tạo mới và xem danh sách nhà hàng
class RestaurantCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Xem, cập nhật, xóa nhà hàng theo ID
class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "pk"

# Tạo mới và xem danh sách menu
class MenuCreate(generics.ListCreateAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenuSerializer

    # Đảm bảo liên kết với nhà hàng theo restaurant_number
    def perform_create(self, serializer):  
        restaurant_number = self.request.data.get("restaurant_number")  # Lấy đúng khóa chính của nhà hàng
        restaurant = get_object_or_404(Restaurant, restaurant_number=restaurant_number)  
        serializer.save(restaurant=restaurant)

# Xem, cập nhật, xóa menu theo menu_number
class MenuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenuSerializer
    lookup_field = "menu_number"  # Sử dụng menu_number thay vì ID (nếu cần)

