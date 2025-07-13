# genero/forms.py
from django import forms
from .models import Genero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']  # Remova 'lista' se ele não existe no model

