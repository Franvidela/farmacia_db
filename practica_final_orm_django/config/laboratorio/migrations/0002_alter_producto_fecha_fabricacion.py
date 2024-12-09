# Generated by Django 4.2.16 on 2024-12-05 22:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_fabricacion',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2015, 1, 1))]),
        ),
    ]
