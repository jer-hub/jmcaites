from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'info')
    search_fields = ['name']

admin.site.register(Event, EventAdmin)