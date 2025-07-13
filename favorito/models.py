# em algum app como `titulo.models` ou um novo app `favoritos`

from django.db import models
from usuario.models import Usuario
from titulo.models import Titulo

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'titulo')  

    def __str__(self):
        return f"{self.usuario.nome} favoritou {self.titulo.titulo}"
