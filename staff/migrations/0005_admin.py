# Generated by Django 4.0.5 on 2022-06-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_staff_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]
