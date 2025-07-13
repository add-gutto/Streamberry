from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        labels = {
            'titulo': 'Nome do Filme',
            'ano_lancamento': 'Ano de Lançamento',
            'sinopse': 'Sinopse',
            'duracao_minutos': 'Duração (em minutos)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'sign__input',
                'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
            })
