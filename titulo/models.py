from django.db import models

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.PositiveIntegerField()
    sinopse = models.TextField()

    class Meta:
        abstract = True  # Define como modelo abstrato

# Filme herda de Titulo
class Filme(Titulo):
    duracao_minutos = models.PositiveIntegerField()
    diretor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - Filme"

# Série herda de Titulo
class Serie(Titulo):
    numero_temporadas = models.PositiveIntegerField()
    criador = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - Série"
