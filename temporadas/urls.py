from django.urls import path
from . import views

app_name = 'temporadas'

urlpatterns = [
    # Temporadas
    path('serie/<int:serie_id>/temporadas/cadastrar/', views.cadastrar_temporada, name='cadastrar_temporada'),
    path('temporada/<int:pk>/editar/', views.editar_temporada, name='editar_temporada'),
    path('temporada/<int:pk>/remover/', views.remover_temporada, name='remover_temporada'),

    # Episódios
    path('temporada/<int:temporada_id>/episodios/cadastrar/', views.cadastrar_episodio, name='cadastrar_episodio'),
    path('episodio/<int:pk>/editar/', views.editar_episodio, name='editar_episodio'),
    path('episodio/<int:pk>/remover/', views.remover_episodio, name='remover_episodio'),
]
