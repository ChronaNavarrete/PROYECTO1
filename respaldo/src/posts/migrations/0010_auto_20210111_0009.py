# Generated by Django 3.1.3 on 2021-01-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210102_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img-perfil-ejemplo.jpg', upload_to='profile_pics'),
        ),
    ]