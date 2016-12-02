from django.http import HttpResponse
from voting.models import UniquePerson, SimpleDayRecord
from django.utils import timezone


def index(request):
    persons = UniquePerson.objects.all()
    days = SimpleDayRecord.objects.all()
    return HttpResponse("Hello, world. Can we make metro easier? <br>"
                        "Allready made " +
                        str(len(days)) +
                        " days simplier to " +
                        str(len(persons)) + " unique persons")


def vote(request):
    now = timezone.now()
    client_ip = request.META['REMOTE_ADDR']
    try:
        unique_person = UniquePerson.objects.get(ip=client_ip)
    except:
        unique_person = UniquePerson(ip=client_ip)
        unique_person.save()

    new_day = SimpleDayRecord(person = unique_person, record_date = now)
    new_day.save()
    return HttpResponse("+1 simple day added")