# Generated by Django 3.2.3 on 2021-06-03 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 14, 13, 5, 386476, tzinfo=utc)),
        ),
    ]
