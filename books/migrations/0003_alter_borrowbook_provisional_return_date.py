# Generated by Django 4.2.2 on 2023-07-19 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='provisional_return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 13, 12, 29, 880267, tzinfo=datetime.timezone.utc)),
        ),
    ]
