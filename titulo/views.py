from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from temporadas.models import Temporada
from .models import  Titulo, Filme , Serie
from .forms import FilmeForm, SerieForm 
from favorito.models import Favorito


def titulos(request):
    filmes = Filme.objects.all()
    series = Serie.objects.all()
    return render (request, "titulo/titulos.html", {'filmes': filmes, 'series': series})

def detail_titulo_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    generos_do_filme = filme.generos.all()
    filmes_relacionados = Filme.objects.filter(generos__in=generos_do_filme).exclude(id=filme.id).distinct()

    favoritado = False
    if request.user.is_authenticated:
        favoritado = Favorito.objects.filter(usuario=request.user, titulo=filme).exists()

    return render(request, "titulo/detail_filme.html", {
        'filme': filme,
        'sugestoes': filmes_relacionados,
        'favoritado': favoritado,
    })

def detail_titulo_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    generos_da_serie = serie.generos.all()
    series_relacionadas = Serie.objects.filter(generos__in=generos_da_serie).exclude(id=serie.id).distinct()
    temporadas = Temporada.objects.filter(serie=serie).order_by('numero').prefetch_related('episodios')
    favoritado = False
    if request.user.is_authenticated:
        favoritado = Favorito.objects.filter(usuario=request.user, titulo=serie).exists()
    
    return render(request, "titulo/detail_series.html", {
        'serie': serie,
        'favoritado': favoritado,
        'temporadas': temporadas,
        'sugestoes': series_relacionadas
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)  # ← Aqui está o ponto crucial!
        if form.is_valid(): 
            form.save() 
            return redirect('listar_filmes') 
    else:
        form = FilmeForm() 
    
    return render(request, 'titulo/form.html', {
        'form': form, 
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title': 'Cadastrar Filme',
        'form_btn': 'Cadastrar'
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)  # importante incluir request.FILES para upload
        if form.is_valid():
            form.save() 
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)  # só instancia para exibir no formulário
    
    return render(request, 'titulo/form.html', {
        'form': form, 
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title': 'Editar Filme',
        'form_btn': 'Salvar Alterações'
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.delete() 
        return redirect('listar_filmes')
    
@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def cadastrar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES)  # ← Corrigido aqui
        if form.is_valid():
            form.save()
            return redirect('listar_series')
    else:
        form = SerieForm()  # ← Só instancia vazio no GET
    
    return render(request, 'titulo/form.html', {
        'form': form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title': 'Cadastrar Série',
        'form_btn': 'Cadastrar'
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def editar_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES, instance=serie)  # ← Corrigido aqui
        if form.is_valid():
            form.save()
            return redirect('listar_series')
    else:
        form = SerieForm(instance=serie)  # ← Correto para GET
    
    return render(request, 'titulo/form.html', {
        'form': form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title': 'Editar Série',
        'form_btn': 'Salvar'
    })


@login_required
@permission_required('usuario.gerenciar_titulos', raise_exception=True)
def remover_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)

    if request.method == 'POST':
        serie.delete()
        return redirect('listar_series')
    

def search(request):
    query = request.GET.get("q", "")
    titulos_com_tipo = []

    if query:
        titulos = Titulo.objects.filter(titulo__icontains=query)

        for titulo in titulos:
            if hasattr(titulo, 'filme'):
                tipo = 'filme'
            elif hasattr(titulo, 'serie'):
                tipo = 'serie'
            else:
                tipo = 'desconhecido'

            titulos_com_tipo.append({
                'titulo': titulo,
                'tipo': tipo
            })

    return render(request, "titulo/search.html", {
        "titulos": titulos_com_tipo,
        "query": query
    })

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'titulo/search_filme.html', {'filmes': filmes})

def listar_series(request):
    series = Serie.objects.all()
    return render(request, 'titulo/search_serie.html', {'series': series})
    
def erro_404(request, exception):
    return render(request, '404.html', status=404)

def erro_500(request):
    return render(request, '500.html', status=500)


