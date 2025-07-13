from django.db import models
from genero.models import Genero

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.PositiveIntegerField()
    sinopse = models.TextField()
    generos = models.ManyToManyField(Genero)

class Filme(Titulo):
    duracao_minutos = models.PositiveIntegerField()
    video_url = models.URLField("Link do vídeo", max_length=500, blank=True, null=True)
    capa = models.ImageField(upload_to='capas_filmes/', blank=True, null=True)
    hls_link = models.URLField("Link HLS (m3u8)", max_length=500, blank=True, null=True)

class Serie(Titulo):
    numero_temporadas = models.PositiveIntegerField()

