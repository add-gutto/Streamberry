from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from temporadas.models import Temporada
from .models import Filme, Serie, Titulo
from .forms import FilmeForm, SerieForm
from favorito.models import Favorito


# =====================
# Listas e detalhes
# =====================
def titulos(request):
    filmes = Filme.objects.all()
    series = Serie.objects.all()
    return render (request, "titulo/titulos.html", {'filmes': filmes, 'series': series})


class FilmeDetailView(DetailView):
    model = Filme
    template_name = "titulo/detail_filme.html"
    context_object_name = "filme"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        generos_do_filme = self.object.generos.all()
        ctx["sugestoes"] = Filme.objects.filter(
            generos__in=generos_do_filme
        ).exclude(id=self.object.id).distinct()
        ctx["favoritado"] = (
            Favorito.objects.filter(usuario=self.request.user, titulo=self.object).exists()
            if self.request.user.is_authenticated else False
        )
        return ctx


class SerieDetailView(DetailView):
    model = Serie
    template_name = "titulo/detail_series.html"
    context_object_name = "serie"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        generos_da_serie = self.object.generos.all()
        ctx["sugestoes"] = Serie.objects.filter(
            generos__in=generos_da_serie
        ).exclude(id=self.object.id).distinct()
        ctx["temporadas"] = Temporada.objects.filter(
            serie=self.object
        ).order_by("numero").prefetch_related("episodios")
        ctx["favoritado"] = (
            Favorito.objects.filter(usuario=self.request.user, titulo=self.object).exists()
            if self.request.user.is_authenticated else False
        )
        return ctx


# =====================
# CRUD de Filme
# =====================
class FilmeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = "titulo/form.html"
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_filmes")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancelar_url"] = self.request.META.get("HTTP_REFERER")
        ctx["form_title"] = "Cadastrar Filme"
        ctx["form_btn"] = "Cadastrar"
        return ctx


class FilmeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = "titulo/form.html"
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_filmes")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancelar_url"] = self.request.META.get("HTTP_REFERER")
        ctx["form_title"] = "Editar Filme"
        ctx["form_btn"] = "Salvar Alterações"
        return ctx


class FilmeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Filme
    template_name = "titulo/confirm_delete.html"  # você pode criar esse template
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_filmes")


# =====================
# CRUD de Série
# =====================
class SerieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Serie
    form_class = SerieForm
    template_name = "titulo/form.html"
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_series")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancelar_url"] = self.request.META.get("HTTP_REFERER")
        ctx["form_title"] = "Cadastrar Série"
        ctx["form_btn"] = "Cadastrar"
        return ctx


class SerieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Serie
    form_class = SerieForm
    template_name = "titulo/form.html"
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_series")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancelar_url"] = self.request.META.get("HTTP_REFERER")
        ctx["form_title"] = "Editar Série"
        ctx["form_btn"] = "Salvar"
        return ctx


class SerieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Serie
    template_name = "titulo/confirm_delete.html"
    permission_required = "usuario.gerenciar_titulos"
    success_url = reverse_lazy("listar_series")


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


