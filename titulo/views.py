# ARQUIVO: titulo/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme # Quando criar a Serie, adicione ", Serie" aqui
from .forms import FilmeForm # Quando criar o form da Serie, adicione ", SerieForm" aqui

# 1. LISTAR todos os filmes
def listar_filmes(request):
    filmes = Filme.objects.all()
    # Usa o template para listar os filmes
    return render(request, 'titulo/lista_filmes.html', {'filmes': filmes})

# 2. CADASTRAR um novo filme
def cadastrar_filme(request):
    # Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid(): # Se os dados são válidos
            form.save() # Salva o novo filme no banco
            return redirect('listar_filmes') # Redireciona para a lista
    # Se for a primeira vez acessando a página (método GET)
    else:
        form = FilmeForm() # Cria um formulário em branco
    
    # Renderiza a página do formulário
    return render(request, 'titulo/form_filme.html', {'form': form})

# 3. EDITAR um filme existente
def editar_filme(request, pk):
    # Pega o filme específico pelo seu 'pk' (ID), ou retorna erro 404 se não existir
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados E com a instância do filme que está sendo editado
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save() # Salva as alterações
            return redirect('listar_filmes')
    else:
        # Preenche o formulário com os dados atuais do filme
        form = FilmeForm(instance=filme)
    
    return render(request, 'titulo/form_filme.html', {'form': form})

# 4. REMOVER um filme
def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    # A exclusão só acontece se o usuário confirmar na página (enviando um POST)
    if request.method == 'POST':
        filme.delete() # Exclui o filme do banco
        return redirect('listar_filmes')
    
    # Mostra a página de confirmação de exclusão
    return render(request, 'titulo/confirm_delete.html', {'filme': filme})

# --- FUTURAMENTE, VOCÊ ADICIONARIA AS VIEWS PARA SÉRIE AQUI ---
# def listar_series(request):
#     ...
# def cadastrar_serie(request):
#     ...