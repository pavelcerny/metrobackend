from django.http import HttpResponse
from voting.models import Person, Record
from django.utils import timezone
from django.views import generic


def index(request):
    persons = Person.objects.all()
    days = Record.objects.all()
    return HttpResponse("Hello, world. Can we make metro easier? <br>"
                        "Allready made " +
                        str(len(days)) +
                        " days simplier to " +
                        str(len(persons)) + " unique persons")


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
    return HttpResponse("+1 simple day added")
