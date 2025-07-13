from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = [
            'nome',
            'ano_lancamento',
            'sinopse',
            'duracao_minutos',
        ]
        labels = {
            'nome': 'Nome do Filme',
            'ano_lancamento': 'Ano de Lançamento',
            'sinopse': 'Sinopse',
            'duracao_minutos': 'Duração (em minutos)',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: O Poderoso Chefão'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 1972'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descreva o filme...'}),
            'duracao_minutos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 175'}),
        }