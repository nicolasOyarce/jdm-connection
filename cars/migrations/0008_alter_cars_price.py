# Generated by Django 4.2.7 on 2023-11-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_rename_quantity_cars_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.IntegerField(),
        ),
    ]
