from django.urls import path
from django.contrib.auth import views as auth_views
from usuario import views as usuario_views
from django.urls import reverse_lazy

urlpatterns = [
    # Assinantes
    path('listar/assinantes/', usuario_views.listar_assinantes, name='listar_assinantes'),
    path('login/', usuario_views.login_view, name='login_view'),
    path('logout/', usuario_views.logout_view, name='logout_view'),
    path('signup/', usuario_views.criarconta, name='signup_assinante'),
    path('desativar/<int:pk>/', usuario_views.desativarconta, name='desativar_assinante'),
    path('reativar/<int:pk>/', usuario_views.reativar_conta, name='reativar_assinante'),
    path('editar/<int:pk>/', usuario_views.editar_assinante, name='editar_assinante'),
    path('perfil/<int:pk>/', usuario_views.visualizar_assinante, name='perfil_assinante'),

    # Administradores
    path('listar/admins/', usuario_views.listar_administradores, name='listar_administradores'),
    path('add/', usuario_views.criar_administrador, name='criar_administrador'),
    path('del/<int:pk>/', usuario_views.desativar_administrador, name='desativar_administrador'),
    path('edit/<int:pk>/', usuario_views.editar_administrador, name='editar_administrador'),
    path('perfil/admin/<int:pk>/', usuario_views.visualizar_administrador, name='perfil_administrador'),

    # Segurança
    path('senha/alterar/<int:pk>/', usuario_views.alterar_senha, name='alterar_senha'),
    path('senha/reset/', usuario_views.iniciar_reset_senha, name='iniciar_reset_senha'),
    path('senha/reset/<uidb64>/<token>/',
        usuario_views.CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('senha/sucesso/', auth_views.PasswordResetCompleteView.as_view(
        template_name='usuario/assinante/reset_sucesso.html'
    ), name='password_reset_complete'),
    path('admin/senha/alterar/<int:pk>/', usuario_views.admin_alterar_senha_usuario, name='admin_alterar_senha_usuario'),
]

