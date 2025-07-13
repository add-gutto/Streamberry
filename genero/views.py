from django.shortcuts import render, get_object_or_404, redirect
from .models import Genero
from titulo.models import Titulo
from .forms import GeneroForm

def cadastrar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = form.save()
            return redirect('visualizar_genero', pk=genero.pk)
    else:
        form = GeneroForm()
    return render(request, 'genero/form.html', {'form': form})


def remover_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('pagina_stream')  # Redireciona usando o nome da view
    return render(request, 'genero/confirm_delete.html', {
        'genero': genero,
        'cancelar_url': request.META.get('HTTP_REFERER')  # Volta para a página anterior
    })


def atualizar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            genero = form.save()
            return redirect('visualizar_genero', pk=genero.pk)
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/form.html', {'form': form})


def buscar_por_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    # Filtra os títulos que têm o gênero selecionado
    titulos = Titulo.objects.filter(generos=genero).distinct()

    # Se quiser enviar tipo para o template (filme ou serie), pode preparar a lista assim:
    titulos_com_tipo = []
    for titulo in titulos:
        tipo = None
        # Tenta saber se é filme ou serie (assumindo herança)
        if hasattr(titulo, 'filme'):
            tipo = 'filme'
        elif hasattr(titulo, 'serie'):
            tipo = 'serie'
        else:
            tipo = 'titulo'  # fallback

        titulos_com_tipo.append({'titulo': titulo, 'tipo': tipo})

    return render(request, 'genero/search.html', {
        'genero': genero,
        'titulos': titulos_com_tipo
    })



