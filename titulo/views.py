from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme, Serie
from .forms import FilmeForm, SerieForm

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'titulo/lista_filmes.html', {'filmes': filmes})

def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'titulo/form_filme.html', {'form': form})

def atualizar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'titulo/form_filme.html', {'form': form})

def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    return render(request, 'titulo/confirm_delete.html', {'titulo': filme})
