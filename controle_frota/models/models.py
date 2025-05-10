from django.db import models

class Veiculo(models.Model):
    TIPO_PLACA_CHOICES = (
        ('OFICIAL', 'Oficial'),
        ('PARTICULAR', 'Particular'),
    )

    GRUPO_CHOICES = (
        ('A', 'Representação'),
        ('B', 'Transporte Institucional'),
        ('C', 'Serviço Comum'),
        ('D', 'Coletivo/Judicial'),
        ('E', 'Carga Leve'),
        ('F', 'Carga Pesada'),
        ('G', 'Apoio Especial'),
        ('H', 'Blindado'),
        ('I', 'Motocicleta'),
        ('X', 'Sem Classificação'),
    )

    placa = models.CharField(max_length=10, unique=True)
    chassi = models.CharField(max_length=50, unique=True)
    numero_motor = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)
    ano_fabricacao = models.PositiveIntegerField()
    tipo_placa = models.CharField(max_length=15, choices=TIPO_PLACA_CHOICES, default='OFICIAL')
    grupo = models.CharField(max_length=1, choices=GRUPO_CHOICES)
    capacidade = models.PositiveIntegerField()
    valor_aquisicao = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=100)
    documento_fornecedor = models.CharField(max_length=100)
    certificado = models.CharField(max_length=50, blank=True, null=True)
    registro_patrimonial = models.CharField(max_length=50, blank=True, null=True)
    seguradora = models.CharField(max_length=100, blank=True, null=True)
    numero_apolice = models.CharField(max_length=50, blank=True, null=True)
    chip_identificacao = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.placa} - {self.modelo} ({self.grupo})"