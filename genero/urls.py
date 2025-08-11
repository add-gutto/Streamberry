from django.urls import path
from .views import GeneroCreateView, GeneroUpdateView, GeneroDeleteView
from . import views

urlpatterns = [
    path('<int:pk>/', views.buscar_por_genero, name='visualizar_genero'),
    path('cadastrar/', GeneroCreateView.as_view(), name='criar_genero'),
    path('editar/<int:pk>/', GeneroUpdateView.as_view(), name='atualizar_genero'),
    path('del/<int:pk>/', GeneroDeleteView.as_view(), name='remover_genero'),
]
