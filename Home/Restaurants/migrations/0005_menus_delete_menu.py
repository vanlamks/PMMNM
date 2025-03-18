# Generated by Django 5.1.7 on 2025-03-17 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0004_users_remove_menu_id_remove_menu_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('menu_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone', models.PositiveBigIntegerField(default=0)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('restaurant_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.restaurant')),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
