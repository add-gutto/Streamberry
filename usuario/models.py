from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# 1. Manager customizado para o modelo Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        # Verifica se email foi informado
        if not email:
            raise ValueError('O email deve ser informado')
        
        # Normaliza o email (coloca em lowercase etc)
        email = self.normalize_email(email)

        # Cria uma instância do usuário com email e nome
        usuario = self.model(email=email, nome=nome, **extra_fields)

        # Define a senha (faz hash)
        usuario.set_password(password)

        # Salva no banco
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, nome, password=None, **extra_fields):
        # Define flags para superusuário
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self.create_user(email, nome, password, **extra_fields)

    # Esse método é necessário para autenticação e criação de superusuário
    def get_by_natural_key(self, email):
        return self.get(email=email)


# 2. Modelo Usuario customizado
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)

    # Campos importantes para o Django admin e sistema de permissões
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'       # Define o campo usado para login
    REQUIRED_FIELDS = ['nome']     # Campos obrigatórios além do USERNAME_FIELD

    objects = UsuarioManager()      # Define o manager customizado para o modelo

    def __str__(self):
        return self.email


# 3. Modelo Assinante relacionado ao Usuario
class Assinante(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
    ]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pausado')
    data_assinatura = models.DateField(auto_now_add=True)
    data_renovacao = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    endereco_cobranca = models.TextField()


# 4. Modelo Administrador relacionado ao Usuario
class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
