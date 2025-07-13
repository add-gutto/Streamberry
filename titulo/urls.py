from django.urls import path
from . import views

urlpatterns = [
    path("", views.titulos, name="pagina_stream"),
    path("search/", views.search, name="search"),
    path("about/", views.central_ajuda, name="central_ajuda"),
    path('list/filme/', views.listar_filmes, name='listar_filmes'),
    path('cadastrar/filme/', views.cadastrar_filme, name='cadastrar_filme'),
    path('editar/filme/<int:pk>/', views.editar_filme, name='editar_filme'),
    path('del/filme/<int:pk>/', views.remover_filme, name='remover_filme'),
    path("detail/filme/<int:pk>/", views.detail_titulo_filme, name="detalhe_titulo_filme"),
    path("detail/serie/", views.detail_titulo_serie, name="detalhe_titulo_serie"),
]
