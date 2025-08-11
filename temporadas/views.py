from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Serie, Temporada, Episodio
from .forms import TemporadaForm, EpisodioForm


# ======== TEMPORADAS ========
class TemporadaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Temporada
    form_class = TemporadaForm
    template_name = 'temporadas/form.html'
    permission_required = 'usuario.gerenciar_titulos'

    def dispatch(self, request, *args, **kwargs):
        self.serie = get_object_or_404(Serie, pk=self.kwargs['serie_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.serie = self.serie
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.serie.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'serie': self.serie,
            'form_title': 'Cadastrar Temporada',
            'form_btn': 'Salvar',
            'cancelar_url': self.request.META.get('HTTP_REFERER')
        })
        return context


class TemporadaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Temporada
    form_class = TemporadaForm
    template_name = 'temporadas/form.html'
    permission_required = 'usuario.gerenciar_titulos'

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.object.serie.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'serie': self.object.serie,
            'form_title': 'Editar Temporada',
            'form_btn': 'Atualizar',
            'cancelar_url': self.request.META.get('HTTP_REFERER')
        })
        return context


class TemporadaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Temporada
    permission_required = 'usuario.gerenciar_titulos'

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.object.serie.id})


# ======== EPISÓDIOS ========
class EpisodioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Episodio
    form_class = EpisodioForm
    template_name = 'temporadas/form.html'
    permission_required = 'usuario.gerenciar_titulos'

    def dispatch(self, request, *args, **kwargs):
        self.temporada = get_object_or_404(Temporada, pk=self.kwargs['temporada_id'])
        self.serie = self.temporada.serie
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['temporada'].queryset = self.serie.temporadas.all()
        return form

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.serie.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'serie': self.serie,
            'temporada': self.temporada,
            'form_title': 'Cadastrar Episódio',
            'form_btn': 'Salvar',
            'cancelar_url': self.request.META.get('HTTP_REFERER')
        })
        return context


class EpisodioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Episodio
    form_class = EpisodioForm
    template_name = 'temporadas/form.html'
    permission_required = 'usuario.gerenciar_titulos'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        serie = self.object.temporada.serie
        form.fields['temporada'].queryset = serie.temporadas.all()
        return form

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.object.temporada.serie.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'temporada': self.object.temporada,
            'form_title': 'Editar Episódio',
            'form_btn': 'Atualizar',
            'cancelar_url': self.request.META.get('HTTP_REFERER')
        })
        return context


class EpisodioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Episodio
    permission_required = 'usuario.gerenciar_titulos'

    def get_success_url(self):
        return reverse_lazy('detalhe_titulo_serie', kwargs={'pk': self.object.temporada.serie.id})
