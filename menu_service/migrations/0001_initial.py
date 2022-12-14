# Generated by Django 4.0.6 on 2022-08-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('info', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'dishes',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'drinks',
            },
        ),
    ]
