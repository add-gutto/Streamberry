from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes, name='listar_filmes'),
    path('cadastrar/', views.cadastrar_filme, name='cadastrar_filme'),
    path('<int:pk>/editar/', views.atualizar_filme, name='atualizar_filme'),
    path('<int:pk>/remover/', views.remover_filme, name='remover_filme'),
]
