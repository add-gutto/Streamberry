from django.apps import AppConfig

class UsuarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usuario"

    def ready(self):
        import usuario.signals  # mantém se estiver usando
        import usuario.permissoes  # apenas importa o arquivo (não executa nada)
