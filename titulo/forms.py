from django import forms
from .models import Filme
from .models import Serie
from genero.models import Genero

class FilmeForm(forms.ModelForm):
    generos = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Gêneros"
    )

    class Meta:
        model = Filme
        fields = '__all__'
        labels = {
            'titulo': 'Nome do Filme',
            'ano_lancamento': 'Ano de Lançamento',
            'sinopse': 'Sinopse',
            'duracao_minutos': 'Duração (em minutos)',
            'generos': 'Gêneros',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'generos':  # NÃO sobrescrever atributos do widget checkbox dos gêneros
                field.widget.attrs.update({
                    'class': 'sign__input',
                    'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
                })

class SerieForm(forms.ModelForm):
    generos = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Gêneros"
    )

    class Meta:
        model = Serie
        fields = '__all__'
        labels = {
            'titulo': 'Nome da Série',
            'ano_lancamento': 'Ano de Lançamento',
            'sinopse': 'Sinopse',
            'numero_temporadas': 'Número de Temporadas',
            'generos': 'Gêneros',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'generos':  # NÃO sobrescrever atributos do widget checkbox dos gêneros
                field.widget.attrs.update({
                    'class': 'sign__input',
                    'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
                })