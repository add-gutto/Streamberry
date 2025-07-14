from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Serie, Temporada, Episodio
from .forms import TemporadaForm, EpisodioForm

@login_required
def listar_temporadas(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    temporadas = Temporada.objects.filter(serie=serie).order_by('numero')
    return render(request, 'temporadas/listar_temporadas.html', {'serie': serie, 'temporadas': temporadas})

@login_required
def listar_episodios(request, temporada_id):
    temporada = get_object_or_404(Temporada, pk=temporada_id)
    episodios = Episodio.objects.filter(temporada=temporada).order_by('numero')
    return render(request, 'temporadas/listar_episodios.html', {'temporada': temporada, 'episodios': episodios})

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def cadastrar_temporada(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    if request.method == 'POST':
        form = TemporadaForm(request.POST)
        if form.is_valid():
            temporada = form.save(commit=False)
            temporada.serie = serie
            temporada.save()
            return redirect('listar_temporadas', serie_id=serie.id)
    else:
        form = TemporadaForm()
    return render(request, 'temporadas/form_temporada.html', {'form': form, 'serie': serie})

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect('listar_temporadas', serie_id=temporada.serie.id)
    else:
        form = TemporadaForm(instance=temporada)
    return render(request, 'temporadas/form_temporada.html', {'form': form, 'serie': temporada.serie})

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    serie_id = temporada.serie.id
    if request.method == 'POST':
        temporada.delete()
        return redirect('listar_temporadas', serie_id=serie_id)

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def cadastrar_episodio(request, temporada_id):
    temporada = get_object_or_404(Temporada, pk=temporada_id)
    if request.method == 'POST':
        form = EpisodioForm(request.POST)
        if form.is_valid():
            episodio = form.save(commit=False)
            episodio.temporada = temporada
            episodio.save()
            return redirect('listar_episodios', temporada_id=temporada.id)
    else:
        form = EpisodioForm()
    return render(request, 'temporadas/form_episodio.html', {'form': form, 'temporada': temporada})

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_episodio(request, pk):
    episodio = get_object_or_404(Episodio, pk=pk)
    if request.method == 'POST':
        form = EpisodioForm(request.POST, instance=episodio)
        if form.is_valid():
            form.save()
            return redirect('listar_episodios', temporada_id=episodio.temporada.id)
    else:
        form = EpisodioForm(instance=episodio)
    return render(request, 'temporadas/form_episodio.html', {'form': form, 'temporada': episodio.temporada})

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_episodio(request, pk):
    episodio = get_object_or_404(Episodio, pk=pk)
    temporada_id = episodio.temporada.id
    if request.method == 'POST':
        episodio.delete()
        return redirect('listar_episodios', temporada_id=temporada_id)
