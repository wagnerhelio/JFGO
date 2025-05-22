from django.db import models
from controle_frota.models import Veiculo

class Requisicao(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Rejeitada', 'Rejeitada'), 
    )

    TIPO_CHOICES = (
        ('Oficial', 'Oficial'),
        ('Particular', 'Particular'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_utilizacao = models.DateField()
    unidade = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    itinerario = models.TextField(blank=True, null=True)

    km_entrada = models.PositiveIntegerField(blank=True, null=True)
    km_saida = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pendente'
    )

    def __str__(self):
        return f"{self.veiculo} - {self.data_utilizacao} ({self.tipo}) - {self.status}"
