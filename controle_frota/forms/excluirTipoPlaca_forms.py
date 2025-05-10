from django import forms

class ExcluirTipoPlacaForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir este tipo de placa")
