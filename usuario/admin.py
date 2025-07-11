from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Titulo  # ou o nome da sua classe

admin.site.register(Titulo)
