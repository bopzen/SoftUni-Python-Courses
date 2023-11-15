# Generated by Django 4.2.4 on 2023-11-14 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='realestatelisting',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0, 'The rating must be between 0.0 and 10.0'), django.core.validators.MaxValueValidator(10, 'The rating must be between 0.0 and 10.0')]),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='release_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1990, 'The release year must be between 1990 and 2023'), django.core.validators.MaxValueValidator(2023, 'The release year must be between 1990 and 2023')]),
        ),
    ]
