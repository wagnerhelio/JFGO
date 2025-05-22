from django import forms

class ExcluirRequisicaoForm(forms.Form):
    confirmar = forms.BooleanField(label="Confirmo que desejo excluir esta requisição")
