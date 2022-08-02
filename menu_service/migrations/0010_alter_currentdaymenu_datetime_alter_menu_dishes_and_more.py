# Generated by Django 4.0.6 on 2022-08-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_service', '0009_remove_menu_restaurant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentdaymenu',
            name='datetime',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dishes',
            field=models.ManyToManyField(related_name='dishes', to='menu_service.dish'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='drinks',
            field=models.ManyToManyField(related_name='drinks', to='menu_service.drink'),
        ),
    ]
