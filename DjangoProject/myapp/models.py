from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)

class Voyage(models.Model):
    depart = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    type_transport = models.CharField(max_length=50)
    date_depart = models.DateField()
    date_retour = models.DateField()

class Hebergement(models.Model):
    destination = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    nombre_personnes = models.IntegerField()
