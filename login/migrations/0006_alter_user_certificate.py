# Generated by Django 4.1.7 on 2023-04-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_user_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='media/certificates'),
        ),
    ]