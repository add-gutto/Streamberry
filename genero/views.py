from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Genero
from titulo.models import Titulo
from .forms import GeneroForm


class GeneroCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'genero/form.html'
    permission_required = 'usuario.gerenciar_genero'

    def get_success_url(self):
        return reverse_lazy('visualizar_genero', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'cancelar_url': self.request.META.get('HTTP_REFERER'),
            'form_title': 'Cadastrar Gênero',
            'form_btn': 'Salvar'
        })
        return context


class GeneroUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'genero/form.html'
    permission_required = 'usuario.gerenciar_genero'

    def get_success_url(self):
        return reverse_lazy('visualizar_genero', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'cancelar_url': self.request.META.get('HTTP_REFERER'),
            'form_title': 'Editar Gênero',
            'form_btn': 'Salvar'
        })
        return context


class GeneroDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Genero
    permission_required = 'usuario.gerenciar_genero'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER') or reverse_lazy('lista_generos')


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



