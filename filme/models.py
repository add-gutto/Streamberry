from django.db import models

# Create your models here.
from titulo.models import Titulo

class Filme(Titulo):
    duracao = models.IntegerField(help_text="Duração em minutos")
    diretor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - Filme"
