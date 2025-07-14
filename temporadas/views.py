from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Serie, Temporada, Episodio
from .forms import TemporadaForm, EpisodioForm

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
            return redirect('detalhe_titulo_serie', temporada.serie.id)
    else:
        form = TemporadaForm()
    
    return render(request, 'temporadas/form.html', {
        'form': form,
        'serie': serie,
        'form_title': 'Cadastrar Temporada',
        'form_btn': 'Salvar',
        'cancelar_url': request.META.get('HTTP_REFERER')
    })

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect('detalhe_titulo_serie', temporada.serie.id)
    else:
        form = TemporadaForm(instance=temporada)
    return render(request, 'temporadas/form.html', {
        'form': form,
        'serie': temporada.serie,
        'form_title': 'Editar Temporada',
        'form_btn': 'Atualizar',
        'cancelar_url': request.META.get('HTTP_REFERER'),
    })

@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    if request.method == 'POST':
        temporada.delete()
        return redirect('detalhe_titulo_serie', temporada.serie.id)


def cadastrar_episodio(request, temporada_id):
    temporada = get_object_or_404(Temporada, pk=temporada_id)
    serie = temporada.serie
    temporadas_da_serie = serie.temporadas.all()

    if request.method == 'POST':
        form = EpisodioForm(request.POST)
        if form.is_valid():
            episodio = form.save(commit=False)
            episodio.save()
            return redirect('detalhe_titulo_serie', pk=serie.id)
    else:
        form = EpisodioForm()
        # aqui você pode filtrar o queryset do campo temporada
        form.fields['temporada'].queryset = temporadas_da_serie

    return render(request, 'temporadas/form.html', {
        'form': form,
        'serie': serie,
        'temporada': temporada,
        'form_title': 'Cadastrar Episódio',
        'form_btn': 'Salvar',
        'cancelar_url': request.META.get('HTTP_REFERER'),
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_episodio(request, pk):
    episodio = get_object_or_404(Episodio, pk=pk)
    serie = episodio.temporada.serie
    temporadas_da_serie = serie.temporadas.all()

    if request.method == 'POST':
        form = EpisodioForm(request.POST, instance=episodio)
        if form.is_valid():
            form.save()
            return redirect('detalhe_titulo_serie', episodio.temporada.serie.id)
    else:
        form = EpisodioForm(instance=episodio)
        # filtra as temporadas disponíveis no campo
        form.fields['temporada'].queryset = temporadas_da_serie

    return render(request, 'temporadas/form.html', {
        'form': form,
        'temporada': episodio.temporada,
        'form_title': 'Editar Episódio',
        'form_btn': 'Atualizar',
        'cancelar_url': request.META.get('HTTP_REFERER'),
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_episodio(request, pk):
    episodio = get_object_or_404(Episodio, pk=pk)
    temporada_id = episodio.temporada.id
    if request.method == 'POST':
        episodio.delete()
        return redirect('detalhe_titulo_serie', episodio.temporada.serie.id)
