# Generated by Django 3.2.5 on 2021-07-13 04:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210713_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 13, 4, 48, 39, 959380, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
