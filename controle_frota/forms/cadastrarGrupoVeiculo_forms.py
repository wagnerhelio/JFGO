from django import forms
from controle_frota.models import GrupoVeiculo

class CadastrarGrupoVeiculoForm(forms.ModelForm):
    class Meta:
        model = GrupoVeiculo
        fields = ['codigo', 'descricao']
