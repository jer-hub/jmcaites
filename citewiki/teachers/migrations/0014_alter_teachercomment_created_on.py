# Generated by Django 3.2.3 on 2021-06-07 06:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0013_alter_teachercomment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachercomment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 6, 35, 44, 50866, tzinfo=utc)),
        ),
    ]
