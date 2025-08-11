from django.urls import path
from .views import (
    TemporadaCreateView,
    TemporadaUpdateView,
    TemporadaDeleteView,
    EpisodioCreateView,
    EpisodioUpdateView,
    EpisodioDeleteView
)

app_name = 'temporadas'

urlpatterns = [
    # Temporadas
    path('cadastrar/serie/<int:serie_id>/', TemporadaCreateView.as_view(), name='cadastrar_temporada'),
    path('editar/<int:pk>/', TemporadaUpdateView.as_view(), name='editar_temporada'),
    path('del/<int:pk>/', TemporadaDeleteView.as_view(), name='remover_temporada'),

    # Episódios
    path('cadastrar/episodio/<int:temporada_id>/', EpisodioCreateView.as_view(), name='cadastrar_episodio'),
    path('editar/episodio/<int:pk>/', EpisodioUpdateView.as_view(), name='editar_episodio'),
    path('del/episodio/<int:pk>/', EpisodioDeleteView.as_view(), name='remover_episodio'),
]
