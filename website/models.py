from django.db import models

# Create your models here.

class Sport(models.Model):
	nom = models.CharField(max_length=20)

	def __str__(self):
		return self.nom

class Terrain(models.Model):
    nom = models.CharField(max_length=100)
    lieu = models.TextField(null=True)
    sport = models.ForeignKey('Sport')
    etat = models.BooleanField()

    def __str__(self):
        return self.nom
 