from django.shortcuts import render

# Create your views here.
# genero/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genero
from .forms import GeneroForm

def cadastrar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_genero')
    else:
        form = GeneroForm()
    return render(request, 'genero/form.html', {'form': form})

def remover_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('visualizar_genero')
    return render(request, 'genero/confirm_delete.html', {'genero': genero})

def atualizar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('visualizar_genero')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/form.html', {'form': form})

def visualizar_genero(request):
    generos = Genero.objects.all()
    return render(request, 'genero/list.html', {'generos': generos})
