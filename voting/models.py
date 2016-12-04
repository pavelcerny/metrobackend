from django.db import models


class Person(models.Model):
    ip = models.CharField(max_length=100)


class Record(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    record_date = models.DateTimeField('date recorded')

