from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Administrador


@receiver(post_migrate)
def configurar_grupos_e_permissoes(sender, **kwargs):

    content_type = ContentType.objects.get_for_model(Administrador)

    p_gerenciar, _ = Permission.objects.get_or_create(
        codename='gerenciar_administradores',
        name='Pode gerenciar administradores',
        content_type=content_type,
    )

    p_visualizar_usuarios, _ = Permission.objects.get_or_create(
        codename='visualizar_usuarios',
        name='Pode visualizar usuários',
        content_type=content_type,
    )

    p_view_administrador, _ = Permission.objects.get_or_create(
        codename='view_administrador',
        name='Pode visualizar administradores',
        content_type=content_type,
    )

    p_editar_administrador, _ = Permission.objects.get_or_create(
        codename='editar_administrador',
        name='Pode editar administradores',
        content_type=content_type,
    )

    # Cria grupos
    gerente_group, _ = Group.objects.get_or_create(name='Gerente')
    moderador_group, _ = Group.objects.get_or_create(name='Moderador')

    # Define permissões por grupo
    gerente_group.permissions.set([
        p_gerenciar,
        p_visualizar_usuarios,
        p_view_administrador,
        p_editar_administrador
    ])

    moderador_group.permissions.set([
        p_editar_administrador,
        p_view_administrador
    ])

    print("Grupos 'Gerente' e 'Moderador' com permissões personalizadas configurados.")


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
        grupo_nome = instance.cargo.capitalize()  # "gerente" → "Gerente"
        grupo = Group.objects.get(name=grupo_nome)

        instance.usuario.groups.clear()
        instance.usuario.groups.add(grupo)
        print(f" Grupo '{grupo_nome}' atribuído ao usuário {instance.usuario.email}")
    except Group.DoesNotExist:
        print(f" Grupo '{grupo_nome}' não existe. Verifique o post_migrate.")
