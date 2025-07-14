from django import forms
from .models import Temporada, Episodio

class TemporadaForm(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = ['numero']  # só o campo número aparece no form
        labels = {
            'numero': 'Número da Temporada',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'sign__input',
                'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
            })



class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = '__all__'
        labels = {
            'temporada': 'Temporada',
            'numero': 'Número do Episódio',
            'titulo': 'Título do Episódio',
            'duracao_minutos': 'Duração (em minutos)',
            'video_url': 'Link do vídeo',
            'hls_link': 'Link HLS (m3u8)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'sign__input',
                'style': 'width: 100%; background-color: #3f3e3e; color: white; border: none; padding: 10px; margin-bottom: 15px;'
            })