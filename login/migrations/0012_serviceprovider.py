# Generated by Django 4.2.1 on 2023-05-22 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_service_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phno', models.TextField()),
                ('district', models.TextField()),
                ('town', models.TextField()),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.service')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
