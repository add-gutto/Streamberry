from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.buscar_por_genero, name='visualizar_genero'),
    path('cadastrar/', views.cadastrar_genero, name='criar_genero'),
    path('editar/<int:pk>/', views.atualizar_genero, name='atualizar_genero'),
    path('del/<int:pk>/', views.remover_genero, name='remover_genero'),
]
