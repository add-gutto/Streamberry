from .models import Genero

def generos_disponiveis(request):
    return {
        'generos_disponiveis': Genero.objects.all()
    }
