from django import forms
from controle_frota.models import Veiculo

class ExcluirVeiculosForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este veículo")
