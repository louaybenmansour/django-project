from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    quantite = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titre

class Membre(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} {self.prenom}"