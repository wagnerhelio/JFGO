from django import forms
from controle_frota.models import Veiculo

class CadastrarVeiculosForm (forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'placeholder': 'AAA0A00'}),
            'valor_aquisicao': forms.NumberInput(attrs={'step': '0.01'}),
            'ano_fabricacao': forms.NumberInput(attrs={'min': 1990}),
        }
