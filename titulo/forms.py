from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme
from .forms import FilmeForm

# LISTAR filmes
def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filme/list.html', {'filmes': filmes})

# CADASTRAR filme
def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filme/form.html', {'form': form})

# EDITAR filme
def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filme/form.html', {'form': form})

# REMOVER filme
def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    return render(request, 'filme/confirm_delete.html', {'filme': filme})
