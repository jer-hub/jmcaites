from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=64, verbose_name='name of event')
    info = models.TextField(max_length=128, verbose_name='Information')
    event_date = models.DateField()

    def __str__(self):
        return self.name
