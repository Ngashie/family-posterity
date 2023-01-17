from django.dg import models

class Members(models.Model):
    lname = models.CharField(max_length=10)
    password = models.Charfield(max_length=8)

class Event(models.Model):
    eventname = models.CharField(max_length=20)
    vibes = models.ImageField()
