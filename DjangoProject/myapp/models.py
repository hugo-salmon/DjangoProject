from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajoutez des champs supplémentaires si nécessaire
    age = models.IntegerField(null=True, blank=True)
