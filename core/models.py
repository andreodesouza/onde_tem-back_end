from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    TIPO_CHOICES = (
        ('usuario', 'Usuário'),
        ('empresa', 'Empresa'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='usuario')
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"