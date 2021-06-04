# Generated by Django 3.2.3 on 2021-06-03 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 14, 33, 41, 665713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(related_name='subjects', to='teachers.Subject'),
        ),
    ]
