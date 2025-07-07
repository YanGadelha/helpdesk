from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    TIPO_USUARIO_CHOICES = (
        ('usuario', 'Usuário'),
        ('tecnico', 'Técnico'),
    )
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='usuario'
    )
    
    def __str__(self):
        return self.username

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
        ('nao_concluido', 'Não Concluído'),
    ]
    
    URGENCY_LEVEL_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    urgency = models.CharField(max_length=20, choices=URGENCY_LEVEL_CHOICES, default='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Comentario(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='comentarios')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comentario = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.user.username} em {self.ordem_servico.title}'