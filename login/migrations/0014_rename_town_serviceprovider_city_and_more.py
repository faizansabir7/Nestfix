# Generated by Django 4.2.1 on 2023-05-29 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_user_phno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='town',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='phno',
        ),
    ]