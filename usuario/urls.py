from django.urls import path
from usuario import views as usuario_views

urlpatterns = [
    path('login/', usuario_views.login_assinante, name='login_assinante'),
    path('logout/', usuario_views.logout_assinante, name='logout_assinante'),
    path('signup/', usuario_views.criarconta, name='signup_assinante'),                     
    path('desativar/', usuario_views.desativarconta, name='desativar_assinante'),        
    path('editar/', usuario_views.editar_assinante, name='editar_assinante'),               
    path('perfil/', usuario_views.visualizar_assinante, name='perfil_assinante'),           
]

