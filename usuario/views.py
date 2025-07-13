from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordResetConfirmView
from .models import  Usuario, Administrador, Assinante
from .forms import ( UsuarioCreateForm, UsuarioChangeForm, AssinanteForm, AdministradorForm, CustomAuthenticationForm, CustomPasswordChangeForm, 
    CustomPasswordResetForm, CustomAdminPasswordChangeForm, CustomSetPasswordForm)
from decouple import config
from django.http import JsonResponse

# views dos titulos para testes de funcionamento
def home(request):
    return render (request, "index.html")

def login_view(request):
    form = CustomAuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        usuario = form.get_user()

        try:
            assinante = Assinante.objects.get(usuario=usuario)
            if assinante.status == 'cancelado':
                return redirect('reativar_assinante', pk=assinante.pk)
        except Assinante.DoesNotExist:
            pass  

        if Assinante.objects.filter(usuario=usuario).exists() or Administrador.objects.filter(usuario=usuario).exists():
            login(request, usuario)
            return redirect('pagina_stream')

        messages.error(request, 'Usuário não é assinante nem administrador.')

    return render(request, 'usuario/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def reativar_conta(request, pk):
    assinante = get_object_or_404(Assinante, pk=pk)

    if request.method == 'POST':
        assinante.status = 'ativo'
        assinante.save()
        login(request, assinante.usuario)
        return redirect('pagina_stream')  
    
    return render(request, 'usuario/assinante/form.html', {
        'assinante': assinante,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Sua conta foi cancelada, Reativar?',
        'form_btn' : 'Reativar'
    })

def criarconta(request):
    if request.method == 'POST':
        usuario_form = UsuarioCreateForm(request.POST)
        assinante_form = AssinanteForm(request.POST)
        if usuario_form.is_valid() and assinante_form.is_valid():
            usuario = usuario_form.save()
            assinante = assinante_form.save(commit=False)
            assinante.usuario = usuario
            assinante.save()
            login(request, usuario)
            return redirect('pagina_stream')
    else:
        usuario_form = UsuarioCreateForm()
        assinante_form = AssinanteForm()

    return render(request, "usuario/assinante/conta.html", {
        'usuario_form': usuario_form,
        'assinante_form': assinante_form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'conta_title' : 'CRIAR CONTA',
        'conta_btn' : 'CRIAR'
    })

@login_required
def desativarconta(request, pk):
    assinante = get_object_or_404(Assinante, pk=pk)
    assinante.status = 'cancelado'
    assinante.save()
    return redirect('home')

@login_required
def editar_assinante(request, pk):
    assinante = get_object_or_404(Assinante, pk=pk)
    usuario = assinante.usuario

    if request.method == 'POST':
        usuario_form = UsuarioChangeForm(request.POST, instance=usuario)
        assinante_form = AssinanteForm(request.POST, instance=assinante)
        
        if usuario_form.is_valid() and assinante_form.is_valid():
            usuario_form.save()
            assinante_form.save()
            return redirect('perfil_assinante', pk=pk)
    
    else:
        usuario_form = UsuarioChangeForm(instance=usuario)
        assinante_form = AssinanteForm(instance=assinante)

    return render(request, "usuario/assinante/conta.html", {
    'usuario_form': usuario_form,
    'assinante_form': assinante_form,
    'cancelar_url': request.META.get('HTTP_REFERER'),
    'conta_title' : 'EDITAR CONTA',
    'conta_btn' : 'SALVAR'
})

@login_required
def visualizar_assinante(request, pk):
    assinante = get_object_or_404(Assinante, pk=pk)
    return render(request, "usuario/assinante/perfil.html", {
        'assinante': assinante
    })
    
@login_required
@permission_required('usuario.visualizar_usuarios', raise_exception=True)
def listar_assinantes(request):
    assinantes = Assinante.objects.select_related('usuario').all()
    return render(request, "usuario/admin/index_assinantes.html", {'assinantes': assinantes})

@login_required
@permission_required('usuario.gerenciar_administradores', raise_exception=True)
def listar_administradores(request):
    administradores = Administrador.objects.select_related('usuario').all()
    return render(request, "usuario/admin/index_administradores.html", {'administradores': administradores})

@login_required
@permission_required('usuario.gerenciar_administradores', raise_exception=True)
def search_administradores(request):
    busca = request.GET.get('q', '')
    administradores = Administrador.objects.select_related('usuario')

    if busca:
        administradores = administradores.filter(usuario__nome__icontains=busca)

    dados = [
        {
            'id': admin.id,
            'nome': admin.usuario.nome,
            'email': admin.usuario.email,
            'cargo': admin.cargo,
            'url_perfil': reverse('perfil_administrador', args=[admin.id])
        }
        for admin in administradores
    ]

    return JsonResponse(dados, safe=False)

@login_required
@permission_required('usuario.visualizar_usuarios', raise_exception=True)
def search_assinantes(request):
    busca = request.GET.get('q', '')
    assinantes = Assinante.objects.select_related('usuario')

    if busca:
        assinantes = assinantes.filter(usuario__nome__icontains=busca)

    dados = [
        {
            'id': assinante.id,
            'nome': assinante.usuario.nome,
            'email': assinante.usuario.email,
            'url_perfil': reverse('perfil_assinante', args=[assinante.id]),
        }
        for assinante in assinantes
    ]

    return JsonResponse(dados, safe=False)

@login_required
@permission_required('usuario.gerenciar_administradores', raise_exception=True)
def criar_administrador(request):
    if request.method == 'POST':
        usuario_form = UsuarioCreateForm(request.POST)
        admin_form = AdministradorForm(request.POST)

        if usuario_form.is_valid() and admin_form.is_valid():
            usuario = usuario_form.save()
            administrador = admin_form.save(commit=False)
            administrador.usuario = usuario
            administrador.save()  
            return redirect('listar_administradores')
    else:
        usuario_form = UsuarioCreateForm()
        admin_form = AdministradorForm()

    return render(request, "usuario/admin/conta.html", {
        'usuario_form': usuario_form,
        'admin_form': admin_form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
         'conta_title' : 'CRIAR ADMIN',
         'conta_btn' : 'CRIAR'
    })

@login_required
@permission_required('usuario.view_administrador', raise_exception=True)
def  visualizar_administrador(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    return render(request, "usuario/admin/perfil.html", {'administrador' : administrador})

@login_required
@permission_required('usuario.gerenciar_administradores', raise_exception=True)
def desativar_administrador(request, pk):
    admin = get_object_or_404(Administrador, pk=pk)
    usuario = admin.usuario
    usuario.delete()
    return redirect('listar_administradores')

@login_required
@permission_required('usuario.editar_administrador', raise_exception=True)
def editar_administrador(request, pk):
    admin = get_object_or_404(Administrador, pk=pk)
    usuario = admin.usuario

    if request.method == 'POST':
        usuario_form = UsuarioChangeForm(request.POST, instance=usuario)
        admin_form = AdministradorForm(request.POST, instance=admin)

        if usuario_form.is_valid() and admin_form.is_valid():
            usuario_form.save()
            admin_form.save()
            return redirect('listar_administradores')
    else:
        usuario_form = UsuarioChangeForm(instance=usuario)
        admin_form = AdministradorForm(instance=admin)

    return render(request, "usuario/admin/conta.html", {
        'usuario_form': usuario_form,
        'admin_form': admin_form,
       'cancelar_url': request.META.get('HTTP_REFERER'),
     'conta_title' : 'EDITAR CONTA',
     'conta_btn' : 'EDITAR'
    })


@login_required
def alterar_senha(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=usuario, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('pagina_stream')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomPasswordChangeForm(user=usuario)

    return render(request, 'usuario/assinante/form.html', {
        'form': form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Atualizar Senha',
        'form_btn' : 'Salvar'
    })

def iniciar_reset_senha(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=True,  
                domain_override= config('DOMAIN_APP'),  
                html_email_template_name='usuario/assinante/email_senha.html',
                subject_template_name='usuario/assinante/email_senha.txt',
            )
            messages.success(request, 'Email para redefinição de senha enviado.')
            return redirect('login_view')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'usuario/assinante/form.html', {
        'form': form,
        'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Esqueceu a senha?',
        'form_btn' : 'Enviar'
    })

@login_required
@permission_required('usuario.gerenciar_administradores', raise_exception=True)
def admin_alterar_senha_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = CustomAdminPasswordChangeForm(usuario, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Senha do usuário {usuario.email} alterada com sucesso.')
            return redirect('listar_administradores')  
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form =CustomAdminPasswordChangeForm(usuario)
    
    return render(request, 'usuario/admin/form.html', {
        'form': form, 
        'usuario': usuario, 
         'cancelar_url': request.META.get('HTTP_REFERER'),
        'form_title' : 'Alterar Senha do Usuário',
        'form_btn' : 'Salvar'})

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuario/assinante/form.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login_view')  # <- vai para o login direto

    def form_valid(self, form):
        messages.success(self.request, 'Senha atualizada com sucesso. Faça login com a nova senha.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Redefinir Senha'
        context['form_btn'] = 'Salvar'
        context['cancelar_url'] = reverse_lazy('login_view')  
        return context
    