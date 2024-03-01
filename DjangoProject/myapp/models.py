from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)

class Flight(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=50)
    departure_date = models.DateField()
    return_date = models.DateField()
    is_reserved = models.BooleanField(default=False)

class Hebergement(models.Model):
    destination = models.CharField(max_length=100)
    return_date = models.DateField()
    departure_date = models.DateField()
    number_of_guests = models.IntegerField()

class Sejour(models.Model):
    lieu = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()

class Activite(models.Model):
    sejour = models.ForeignKey(Sejour, on_delete=models.CASCADE)
    jour = models.CharField(max_length=50)
    activite = models.CharField(max_length=255)