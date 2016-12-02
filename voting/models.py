from django.db import models


class UniquePerson(models.Model):
    ip = models.CharField(max_length=100)


class SimpleDayRecord(models.Model):
    person = models.ForeignKey(UniquePerson, on_delete=models.CASCADE)
    record_date = models.DateTimeField('date recorded')

