from django import forms
from .models import Filme
import json

class FilmeForm(forms.ModelForm):
    idioma_disponivel = forms.CharField(
        widget=forms.Textarea,
        help_text="Portugues, Ingles, Espanhol"
    )

    class Meta:
        model = Filme
        fields = ['titulo', 'descricao', 'idioma_disponivel', 'duracao', 'diretor']

    def clean_idioma_disponivel(self):
        data = self.cleaned_data['idioma_disponivel']
        lista = [x.strip() for x in data.split(',') if x.strip()]
        return json.dumps(lista)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.idioma_disponivel = self.cleaned_data['idioma_disponivel']
        if commit:
            instance.save()
        return instance
