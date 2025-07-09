from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Administrador

@receiver(post_migrate)
def criar_admin_padrao(sender, **kwargs):
    Usuario = get_user_model()
    if not Usuario.objects.filter(email='admin@gerente.com').exists():
        usuario = Usuario.objects.create_superuser(
            email='admin@gerente.com',
            nome='Administrador Padrão',
            password='admin123'
        )
        administrador = Administrador.objects.create(
            usuario=usuario,
            cargo='gerente',
        )

        try:
            grupo_gerente = Group.objects.get(name='Gerente')
            usuario.groups.add(grupo_gerente)
            print(" Administrador padrão criado com grupo Gerente.")
        except Group.DoesNotExist:
            print(" Grupo 'Gerente' não encontrado. Execute 'migrate' novamente.")


@receiver(post_save, sender=Administrador)
def atribuir_grupo_automatico(sender, instance, **kwargs):
    try:
        grupo_nome = instance.cargo.capitalize()  
        grupo = Group.objects.get(name=grupo_nome)

        instance.usuario.groups.clear()
        instance.usuario.groups.add(grupo)
        print(f" Grupo '{grupo_nome}' atribuído ao usuário {instance.usuario.email}")
    except Group.DoesNotExist:
        print(f" Grupo '{grupo_nome}' não existe. Verifique o post_migrate.")
