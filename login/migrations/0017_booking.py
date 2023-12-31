# Generated by Django 4.2.1 on 2023-06-16 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_serviceprovider_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('viewed_at', models.DateTimeField(blank=True, null=True)),
                ('sp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.serviceprovider')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
