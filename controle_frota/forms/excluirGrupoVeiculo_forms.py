from django import forms

class ExcluirGrupoVeiculoForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este grupo de veículo")
