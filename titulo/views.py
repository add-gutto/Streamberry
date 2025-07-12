from django.shortcuts import render

# Create your views here.
from .models import Titulo
from .forms import TituloForm

# Cadastrar título
def cadastrar_titulo(request):
    if request.method == 'POST':
        form = TituloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_titulo')
    else:
        form = TituloForm()
    return render(request, 'titulos/form.html', {'form': form})

# Remover título
def remover_titulo(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    if request.method == 'POST':
        titulo.delete()
        return redirect('visualizar_titulo')
    return render(request, 'titulos/confirm_delete.html', {'titulo': titulo})

# Atualizar título
def atualizar_titulo(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    if request.method == 'POST':
        form = TituloForm(request.POST, instance=titulo)
        if form.is_valid():
            form.save()
            return redirect('visualizar_titulo')
    else:
        form = TituloForm(instance=titulo)
    return render(request, 'titulos/form.html', {'form': form})

# Visualizar títulos (lista)
def visualizar_titulo(request):
    titulos = Titulo.objects.all()
    return render(request, 'titulos/list.html', {'titulos': titulos})

