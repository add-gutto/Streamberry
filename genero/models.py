from django.db import models

# Create your models here.
# genero/models.py
from django.db import models
from titulo.models import Titulo

class Genero(models.Model):
    nome = models.CharField(max_length=100)
    lista = models.ManyToManyField(Titulo, related_name='generos')

    def __str__(self):
        return self.nome
