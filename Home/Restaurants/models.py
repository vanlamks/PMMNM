from django.db import models 
from django.utils.timezone import now

class Restaurant(models.Model):
    restaurant_number = models.CharField(max_length=50, unique=True, primary_key=True)  # Mã nhà hàng là PK
    restaurant_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    class Meta:
        db_table = 'restaurants_restaurant'

    def __str__(self):
        return self.restaurant_name

class Menus(models.Model):
    menu_number = models.CharField(max_length=50, primary_key=True)
    menu_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.PositiveBigIntegerField(default=0)  # Lưu số điện thoại dạng số
    description = models.TextField()
    image_url = models.URLField()
    restaurant_number = models.ForeignKey(
        'Restaurants.Restaurant',  # Khóa ngoại đến bảng restaurant
        on_delete=models.CASCADE
    )


