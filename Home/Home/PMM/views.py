from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Restaurant, User
from .serializers import RestaurantSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# API chào mừng
class WelcomeAPI(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the restaurant API!"})

# API tạo mới và xem danh sách nhà hàng
class RestaurantCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# API xem, cập nhật, xóa nhà hàng theo ID
class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "pk"



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Đảm bảo filter chuẩn theo restaurant_number nếu có
    def get_queryset(self):
        restaurant_number = self.request.query_params.get('restaurant_number')
        if restaurant_number:
            return User.objects.filter(restaurant_number=restaurant_number)
        return User.objects.all()

    # Hàm tạo user mới
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            restaurant = Restaurant.objects.get(restaurant_number=data['restaurant_number'])
            user = User.objects.create(
                user_number=data['user_number'],
                full_name=data['full_name'],
                email=data['email'],
                password_hash=data['password_hash'],
                restaurant_number=restaurant
            )
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_400_BAD_REQUEST)
