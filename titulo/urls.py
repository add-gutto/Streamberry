from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_titulos, name='listar_titulos'),
    path('cadastrar/', views.cadastrar_titulo, name='cadastrar_titulo'),
    path('<int:pk>/', views.visualizar_titulo, name='visualizar_titulo'),
    path('<int:pk>/editar/', views.atualizar_titulo, name='atualizar_titulo'),
    path('<int:pk>/remover/', views.remover_titulo, name='remover_titulo'),
]
