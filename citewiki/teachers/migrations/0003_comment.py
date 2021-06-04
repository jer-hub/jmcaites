# Generated by Django 3.2.3 on 2021-06-03 14:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20210603_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('body', models.TextField(default='null')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2021, 6, 3, 14, 2, 29, 956856, tzinfo=utc))),
                ('active', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='teachers.teacher')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
