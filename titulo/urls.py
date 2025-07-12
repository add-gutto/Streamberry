
from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('filmes/cadastrar/', views.cadastrar_filme, name='cadastrar_filme'),
    path('filmes/<int:pk>/editar/', views.editar_filme, name='editar_filme'),
    path('filmes/<int:pk>/remover/', views.remover_filme, name='remover_filme'),
]
