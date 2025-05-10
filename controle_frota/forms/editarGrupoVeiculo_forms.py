from django import forms
from controle_frota.models import GrupoVeiculo

class EditarGrupoVeiculoForm(forms.ModelForm):
    class Meta:
        model = GrupoVeiculo
        fields = ['codigo', 'descricao']
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Ex: A'}),
            'descricao': forms.TextInput(attrs={'placeholder': 'Representação'}),
        }