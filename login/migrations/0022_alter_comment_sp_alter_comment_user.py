# Generated by Django 4.2.1 on 2023-06-21 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_booking_city_booking_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.serviceprovider'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
