from django.urls import path
from .views import RestaurantCreate
from .views import RestaurantRetrieveUpdateDestroy
from .views import MenuCreate
from .views import MenuRetrieveUpdateDestroy

urlpatterns = [
    path('v/', RestaurantCreate.as_view(), name="restaurant-view-create"),
    path('v/<int:pk>',RestaurantRetrieveUpdateDestroy.as_view(), name="update"),
     path('m/', MenuCreate.as_view(), name="restaurant-view-create"),
    path('m/<int:pk>',MenuRetrieveUpdateDestroy.as_view(), name="update"),
]
