# Generated by Django 4.0.6 on 2022-07-20 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2022, 7, 20), verbose_name='День рождения'),
        ),
    ]
