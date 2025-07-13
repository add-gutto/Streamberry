# favoritos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('minha-lista/', views.minha_lista, name='minha_lista'),
    path('favoritar/<int:pk>/', views.adicionar_favorito, name='adicionar_favorito'),
    path('remover/<int:pk>/', views.remover_favorito, name='remover_favorito'),
]
