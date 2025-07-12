from .models import Titulo
import json

class TituloForm(forms.ModelForm):
    idiomadisponivel = forms.CharField(
        widget=forms.Textarea,
        help_text="Portugues, Ingles, Espanhol"
    )

    class Meta:
        model = Titulo
        fields = ['titulo', 'descricao', 'idiomadisponivel']

    def clean_idiomadisponivel(self):
        data = self.cleaned_data['idiomadisponivel']
        # transforma string "pt, en, es" em lista ["pt", "en", "es"]
        lista = [x.strip() for x in data.split(',') if x.strip()]
        return json.dumps(lista)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # idiomadisponivel já está como JSON na cleaned_data
        instance.idiomadisponivel = self.cleaned_data['idiomadisponivel']
        if commit:
            instance.save()
        return instance