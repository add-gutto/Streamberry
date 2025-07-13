from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Administrador

@receiver(post_migrate)
def criar_grupos_e_permissoes(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Administrador)

    # Permissões
    permissoes = [
        {'codename': 'gerenciar_administradores', 'name': 'Pode gerenciar administradores'},
        {'codename': 'visualizar_usuarios', 'name': 'Pode visualizar usuários'},
        {'codename': 'view_administrador', 'name': 'Pode visualizar administradores'},
        {'codename': 'editar_administrador', 'name': 'Pode editar administradores'},
        {'codename': 'gerenciar_titulos', 'name': 'Pode gerenciar Titulos'},
        {'codename': 'gerenciar_genero', 'name': 'Pode gerenciar Genero'},
    ]

    permissoes_objs = []
    for p in permissoes:
        perm, _ = Permission.objects.get_or_create(
            codename=p['codename'],
            name=p['name'],
            content_type=content_type,
        )
        permissoes_objs.append(perm)

    # Grupos
    gerente_group, _ = Group.objects.get_or_create(name='Gerente')
    moderador_group, _ = Group.objects.get_or_create(name='Moderador')

    # Atribuição
    gerente_group.permissions.set(permissoes_objs)
    moderador_group.permissions.set([
        Permission.objects.get(codename='editar_administrador'),
        Permission.objects.get(codename='view_administrador'),
         Permission.objects.get(codename='gerenciar_titulos'),
          Permission.objects.get(codename='gerenciar_genero'),
    ])
