from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Genero
from titulo.models import Titulo
from .forms import GeneroForm

@login_required
@permission_required('usuario.gerenciar_genero', raise_exception=True)
def cadastrar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = form.save()
            return redirect('visualizar_genero', pk=genero.pk)
    else:
        form = GeneroForm()
    return render(request, 'genero/form.html', {'form': form, 
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Cadastrar Genero',
        'form_btn' : 'Salvar'})

@login_required
@permission_required('usuario.gerenciar_genero', raise_exception=True)
def remover_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect(request.META.get('HTTP_REFERER'))  

@login_required
@permission_required('usuario.gerenciar_genero', raise_exception=True)
def atualizar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            genero = form.save()
            return redirect('visualizar_genero', pk=genero.pk)
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/form.html', {'form': form, 'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Editar Genero',
        'form_btn' : 'Salvar' })


def buscar_por_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    titulos = Titulo.objects.filter(generos=genero).distinct()

    titulos_com_tipo = []
    for titulo in titulos:
        tipo = None
        if hasattr(titulo, 'filme'):
            tipo = 'filme'
        elif hasattr(titulo, 'serie'):
            tipo = 'serie'
        else:
            tipo = 'titulo'  

        titulos_com_tipo.append({'titulo': titulo, 'tipo': tipo})

    return render(request, 'genero/search.html', {
        'genero': genero,
        'titulos': titulos_com_tipo
    })



