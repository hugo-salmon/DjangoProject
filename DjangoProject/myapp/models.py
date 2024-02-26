from django.db import models

class Etudiant(models.Model):
    name = models.CharField(max_length=250)
    prenom = models.TextField()
    age = models.IntegerField()
    photo = models.ImageField()
    tel = models.TextField()
    mail = models.EmailField()
    birth_date = models.DateField()
    place = models.TextField()
    adresse = models.TextField()
    def __str__(self):
        return f"{self.name} {self.prenom} - {self.age} ans"

    def get_info(self):
        return f"Nom: {self.name}\nPrénom: {self.prenom}\nAge: {self.age}\nTéléphone: {self.tel}\nEmail: {self.mail}\nDate de naissance: {self.birth_date}\nLieu: {self.place}\nAdresse: {self.adresse}"
