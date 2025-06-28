from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Assinante, Administrador

class UsuarioCreateForm(UserCreationForm):
    class  Meta: 
        model = Usuario
        fields = ['email', 'nome', 'password1', 'password2']

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome']

class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = ['telefone', 'endereco_cobranca']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['cargo', 'is_superadmin', 'is_staff']
