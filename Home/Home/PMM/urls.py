from django.urls import path, include
from .views import RestaurantCreate, RestaurantRetrieveUpdateDestroy,  UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
      path('v', RestaurantCreate.as_view(), name="restaurant-view-create"),
    path('v<int:pk>/', RestaurantRetrieveUpdateDestroy.as_view(), name="update"),

     path('api/', include(router.urls)),
]
