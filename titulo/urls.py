from django.urls import path
from titulo import views as  titulo_views
from .views import (
    FilmeDetailView,
    SerieDetailView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView,
    SerieCreateView,
    SerieUpdateView,
    SerieDeleteView,
)

urlpatterns = [
    path("", titulo_views.titulos, name="pagina_stream"),
    path("search/", titulo_views.search, name="search"),

    path("list/filme/", titulo_views.listar_filmes, name="listar_filmes"),
    path("cadastrar/filme/", FilmeCreateView.as_view(), name="cadastrar_filme"),
    path("editar/filme/<int:pk>/", FilmeUpdateView.as_view(), name="editar_filme"),
    path("del/filme/<int:pk>/", FilmeDeleteView.as_view(), name="remover_filme"),
    path("detail/filme/<int:pk>/", FilmeDetailView.as_view(), name="detalhe_titulo_filme"),

    path("list/serie/", titulo_views.listar_series, name="listar_series"),
    path("cadastrar/serie/", SerieCreateView.as_view(), name="cadastrar_serie"),
    path("editar/serie/<int:pk>/", SerieUpdateView.as_view(), name="editar_serie"),
    path("del/serie/<int:pk>/", SerieDeleteView.as_view(), name="remover_serie"),
    path("detail/serie/<int:pk>/", SerieDetailView.as_view(), name="detalhe_titulo_serie"),
]
