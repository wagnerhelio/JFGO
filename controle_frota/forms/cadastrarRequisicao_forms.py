from django import forms
from controle_frota.models import Requisicao

class CadastrarRequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = '__all__'
        widgets = {
            'data_utilizacao': forms.DateInput(attrs={'type': 'date'}),
            'km_entrada': forms.NumberInput(attrs={'placeholder': 'Km de entrada'}),
            'km_saida': forms.NumberInput(attrs={'placeholder': 'Km de saída'}),
        }
