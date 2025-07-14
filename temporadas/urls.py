from django.urls import path
from . import views

app_name = 'temporadas'

urlpatterns = [
    # Temporadas
    path('cadastrar/serie/<int:serie_id>/', views.cadastrar_temporada, name='cadastrar_temporada'),
    path('editar/<int:pk>/', views.editar_temporada, name='editar_temporada'),
    path('del/<int:pk>/', views.remover_temporada, name='remover_temporada'),

    # Episódios
    path('cadastrar/episodio/<int:temporada_id>/', views.cadastrar_episodio, name='cadastrar_episodio'),
    path('editar/episodio/<int:pk>/', views.editar_episodio, name='editar_episodio'),
    path('del/episodio/<int:pk>/', views.remover_episodio, name='remover_episodio'),
]
