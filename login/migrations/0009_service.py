# Generated by Django 4.2.1 on 2023-05-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
