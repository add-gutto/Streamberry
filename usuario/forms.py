from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, 
    PasswordResetForm, AdminPasswordChangeForm, SetPasswordForm
)
from .models import Usuario, Assinante, Administrador

class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'password1', 'password2']
        labels = {
            'email': '',
            'nome': '',
            'password1': '',
            'password2': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remover labels
        for field in self.fields.values():
            field.label = ""

        # Estilizar campos
        self.fields['email'].widget.attrs.update({
            'class': 'sign__input',
            'placeholder': 'Email',
            'style': 'width: 100%;'
        })
        self.fields['nome'].widget.attrs.update({
            'class': 'sign__input',
            'placeholder': 'Nome completo',
            'style': 'width: 100%;'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'sign__input',
            'placeholder': 'Senha',
            'style': 'width: 100%; max-width: 350px;'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'sign__input',
            'placeholder': 'Confirme sua senha',
            'style': 'width: 100%; max-width: 350px;'
        })

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'sign__input',
                'placeholder': 'Email',
                'style': 'width: 100%;'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'sign__input',
                'placeholder': 'Nome completo',
                'style': 'width: 100%;'
            })}
        labels = {
            'email': '',
            'nome': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove o campo password para não aparecer no formulário
        if 'password' in self.fields:
            self.fields.pop('password')

class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = ['telefone', 'endereco_cobranca']
        labels = {
            'telefone': '',
            'endereco_cobranca': '',
        }

        widgets = {
            'telefone': forms.TextInput(attrs={
                'class': 'sign__input',
                'placeholder': 'Telefone',
                'style': 'width: 100%; max-width: 400px;'
            }),
            'endereco_cobranca': forms.TextInput(attrs={
                'class': 'sign__input',
                'placeholder': 'Endereço',
                'style': 'width: 100%;'
            }),
        }


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['cargo']
        widgets = {
            'cargo': forms.Select(attrs={
                'class': 'sign__input',
                'style': 'width: 100%; max-width: 400px;',
                'placeholder': 'Cargo'
            }),
        }
        labels = {
            'cargo': '',  # Remove o label se você quiser só o placeholder
        }

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        placeholders = {
            'username': 'Email',
            'password': 'Senha',
        }
        for name, field in self.fields.items():
            field.label = ''
            field.widget.attrs.update({
                'class': 'sign__input',
                'placeholder': placeholders.get(name, ''),
                'style': 'width: 100%; background-color: #3f3e3e;'
            })

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        placeholders = {
            'old_password': 'Senha atual',
            'new_password1': 'Nova senha',
            'new_password2': 'Confirme a nova senha',
        }
        for name, field in self.fields.items():
            field.label = ''
            field.widget.attrs.update({
                'class': 'sign__input',
                'placeholder': placeholders.get(name, ''),
                'style': 'width: 100%; background-color: #3f3e3e;'
            })

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        placeholders = {
            'email': 'Digite seu e-mail',
        }
        for name, field in self.fields.items():
            field.label = ''
            field.widget.attrs.update({
                'class': 'sign__input',
                'placeholder': placeholders.get(name, ''),
                'style': 'width: 100%; background-color: #3f3e3e;'
            })

class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'password1': 'Nova senha',
            'password2': 'Confirme a nova senha',
        }

        for name in list(self.fields.keys()):
            if name not in placeholders.keys():
                self.fields.pop(name)

        for name, field in self.fields.items():
            field.label = ''
            field.widget.attrs.update({
                'class': 'sign__input',
                'placeholder': placeholders.get(name, ''),
                'style': 'width: 100%; background-color: #3f3e3e;'
            })

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'new_password1': 'Nova senha',
            'new_password2': 'Confirme a nova senha',
        }
        for name, field in self.fields.items():
            field.label = ''
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'sign__input',
                'placeholder': placeholders.get(name, ''),
                'style': 'width: 100%; background-color: #3f3e3e;',
            })



