from django.shortcuts import render, get_object_or_404, redirect
from .models import  Titulo, Filme , Serie
from .forms import FilmeForm 

def home(request):
    return render (request, "index.html")

def central_ajuda(request):
    return render(request, "titulo/about.html")

def titulos(request):
    filmes = Filme.objects.all()
    series = Serie.objects.all()
    return render (request, "titulo/titulos.html", {'filmes': filmes, 'series': series})

def detail_titulo_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    # Gêneros do filme atual
    generos_do_filme = filme.generos.all()

    # Títulos (filmes ou séries) com ao menos um gênero em comum, excluindo o próprio
    titulos_relacionados = Titulo.objects.filter(
        generos__in=generos_do_filme
    ).exclude(id=filme.id).distinct()

    return render(request, "titulo/detail_filme.html", {
        'filme': filme,
        'sugestoes': titulos_relacionados
    })


def detail_titulo_serie(request):
    #serie = get_object_or_404(Serie, pk= pk)
    return render (request, "titulo/detail_serie.html")

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

def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('listar_filmes') 
    else:
        form = FilmeForm() 
    
    return render(request, 'titulo/form.html', 
    {
        'form': form, 
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Cadastrar Filme',
        'form_btn' : 'Cadastrar'})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save() 
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
    
    return render(request, 'titulo/form.html', 
    {
        'form': form, 
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Cadastrar Filme',
        'form_btn' : 'Cadastrar'})

def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.delete() 
        return redirect('listar_filmes')

