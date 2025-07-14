# genero/forms.py
from django import forms
from .models import Genero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']  # Remova 'lista' se ele não existe no model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'sign__input',
                'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
            })

