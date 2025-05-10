from django import forms
from controle_frota.models import Veiculo

class EditarVeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'readonly': 'readonly'}),
            'valor_aquisicao': forms.NumberInput(attrs={'step': '0.01'}),
        }
