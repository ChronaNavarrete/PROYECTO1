# Generated by Django 3.1.3 on 2020-12-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabildos', '0007_auto_20201212_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabildo',
            old_name='etiquetas',
            new_name='conceptos',
        ),
    ]