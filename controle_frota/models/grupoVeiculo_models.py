from django.db import models

class GrupoVeiculo (models.Model):
    codigo = models.CharField(max_length=2, unique=True) 
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"