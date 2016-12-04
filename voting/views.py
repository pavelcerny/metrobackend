from django.http import HttpResponse
from voting.models import Person, Record
from django.utils import timezone
from django.template import loader
from django.shortcuts import redirect


def index(request):
    persons = Person.objects.all()
    days = Record.objects.all()
    template = loader.get_template('voting/homepage.html')
    context = {
        'n_persons': len(persons),
        'n_days': len(days)
    }
    return HttpResponse(template.render(context, request))


def after_voting(request):
    persons = Person.objects.all()
    days = Record.objects.all()
    template = loader.get_template('voting/homepage.html')
    context = {
        'voted': True,
        'n_persons': len(persons),
        'n_days': len(days)
    }
    return HttpResponse(template.render(context, request))


def vote(request):
    now = timezone.now()
    client_ip = request.META['REMOTE_ADDR']
    try:
        p = Person.objects.get(ip=client_ip)
    except:
        p = Person(ip=client_ip)
        p.save()

    new_day = Record(person = p, record_date = now)
    new_day.save()
    return redirect('/voted')