from django import forms
from controle_frota.models import Veiculo, GrupoVeiculo, TipoPlaca

class ListarVeiculosForm(forms.Form):
    grupo = forms.ModelChoiceField(
        queryset=GrupoVeiculo.objects.all(),
        required=False,
        label='Grupo do Veículo'
    )
    tipo_placa = forms.ModelChoiceField(
        queryset=TipoPlaca.objects.all(),
        required=False,
        label='Tipo de Placa'
    )
    placa = forms.CharField(
        max_length=10,
        required=False,
        label='Placa (contém)'
    )
