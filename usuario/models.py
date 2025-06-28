from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['nome']

class Assinante(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
    ]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pausado',  
    )        
    data_assinatura = models.DateField(auto_now_add=True)            
    data_renovacao = models.DateField(blank=True, null=True)             
    telefone = models.CharField(max_length=20)                            
    endereco_cobranca = models.TextField()                                

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)             
    is_superadmin = models.BooleanField(default=False)         
    is_staff = models.BooleanField(default=False)          
