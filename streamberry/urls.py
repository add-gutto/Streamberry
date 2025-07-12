"""
URL configuration for streamberry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from usuario import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/", include("usuario.urls")),
    path("", views.home, name= "home"),
    path("titulos/", views.titulos, name="pagina_stream"),
    path("titulos/detail/filme/", views.detail_titulo_filme, name="detalhe_titulo_filme"),
    path("titulos/detail/serie/", views.detail_titulo_serie, name="detalhe_titulo_serie"),
    path("titulos/search/", views.search, name="search")
]

from django.urls import path, include

urlpatterns = [
    path('filmes/', include('filme.urls')),
    path('titulos/', include('titulo.urls')),
]
