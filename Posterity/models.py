from django.dg import models

class Members(models.Model):
    lname = models.CharField(max_length=5)
    password = models.Charfield(max_length=8)