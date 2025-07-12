from django.db import models

# Create your models here.
# 5. Modelo Titulo
class Titulo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    idioma_disponivel = models.JSONField()

    def __str__(self):
        return self.titulo
