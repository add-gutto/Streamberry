from django.shortcuts import get_object_or_404, render
from .models import Favorito
from titulo.models import Titulo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def adicionar_favorito(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    Favorito.objects.get_or_create(usuario=request.user, titulo=titulo)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remover_favorito(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    Favorito.objects.filter(usuario=request.user, titulo=titulo).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def minha_lista(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('titulo')

    titulos = []
    for fav in favoritos:
        titulo = fav.titulo
        if hasattr(titulo, 'filme'):
            tipo = 'filme'
        elif hasattr(titulo, 'serie'):
            tipo = 'serie'
        else:
            tipo = 'desconhecido'

        titulos.append({
            'titulo': titulo,
            'tipo': tipo
        })

    return render(request, 'favorito/search.html', {
        'titulos': titulos
    })
