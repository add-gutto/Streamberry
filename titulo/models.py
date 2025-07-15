import os
import uuid
from django.db import models
from genero.models import Genero

def gerar_nome_arquivo(instance, filename):
    ext = filename.split('.')[-1]
    novo_nome = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('capas', novo_nome)

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.PositiveIntegerField()
    sinopse = models.TextField()
    generos = models.ManyToManyField(Genero)
    capa = models.ImageField(upload_to=gerar_nome_arquivo, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Filme(Titulo):
    duracao_minutos = models.PositiveIntegerField()
    video_url = models.URLField("Link do vídeo", max_length=500, blank=True, null=True)
    hls_link = models.URLField("Link HLS (m3u8)", max_length=500, blank=True, null=True)

class Serie(Titulo):
    hls_link_trailler = models.URLField("Link HLS (m3u8)", max_length=500, blank=True, null=True)


