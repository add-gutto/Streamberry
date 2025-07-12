# genero/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar_genero, name='visualizar_genero'),
    path('cadastrar/', views.cadastrar_genero, name='cadastrar_genero'),
    path('<int:pk>/editar/', views.atualizar_genero, name='atualizar_genero'),
    path('<int:pk>/remover/', views.remover_genero, name='remover_genero'),
]
