from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import Event
from .forms import EventForm
# Create your views here.

def index(request):
    events = Event.objects.all()
    jan = Event.objects.filter(event_date__month="01")
    feb = Event.objects.filter(event_date__month="02")
    mar = Event.objects.filter(event_date__month="03")
    apr = Event.objects.filter(event_date__month="04")
    may = Event.objects.filter(event_date__month="05")
    jun = Event.objects.filter(event_date__month="06")
    jul = Event.objects.filter(event_date__month="07")
    aug = Event.objects.filter(event_date__month="08")
    sept = Event.objects.filter(event_date__month="09")
    octo = Event.objects.filter(event_date__month="10")
    nov = Event.objects.filter(event_date__month="11")
    dec = Event.objects.filter(event_date__month="12")
    return render(request, 'events/index.html', {
        'events': events,
        'jan': jan,
        'feb': feb,
        'mar': mar,
        'apr': apr,
        'may': may,
        'jun': jun,
        'jul': jul,
        'aug': aug,
        'sept': sept,
        'oct': octo,
        'nov': nov,
        'dec': dec
    })

@login_required
def add(request):
    form = EventForm()
    return render(request, 'events/add.html', {
        'form': form
    })

@login_required
def process_add(request):
    name = request.POST.get('name')
    info = request.POST.get('info')
    event_date = request.POST.get('event_date')

    try:
        n = Event.objects.get(name=name)
        # number  already exists
        return render(request, 'events/add.html', {
            'error_msg': "Duplicated event: " + name
        })

    except ObjectDoesNotExist:
        event = Event.objects.create(name=name, info=info, event_date=event_date)

        event.save()
        return HttpResponseRedirect('/calendar_of_events')