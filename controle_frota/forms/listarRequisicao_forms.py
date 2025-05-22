from django import forms

class ListarRequisicaoForm(forms.Form):
    data_utilizacao = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    unidade = forms.CharField(max_length=100, required=False)
