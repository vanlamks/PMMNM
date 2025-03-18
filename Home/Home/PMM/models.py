from django.db import models

# Create your models here.
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
        db_table = 'restaurants'

    def __str__(self):
        return self.restaurant_name


class User(models.Model):
    user_number = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'  # Trùng với tên bảng trong MySQL

    def __str__(self):
        return self.full_name
