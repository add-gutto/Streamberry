from django.db import models
from titulo.models import Serie


class Temporada(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='temporadas')
    numero = models.PositiveIntegerField() 
    
class Episodio(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name='episodios')
    numero = models.PositiveIntegerField()
    titulo = models.CharField(max_length=255)
    duracao_minutos = models.PositiveIntegerField()
    video_url = models.URLField("Link do vídeo", max_length=500, blank=True, null=True)
    hls_link = models.URLField("Link HLS (m3u8)", max_length=500, blank=True, null=True)
