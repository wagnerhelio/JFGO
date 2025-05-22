from django import forms
from controle_frota.models import Requisicao

class EditarStatusRequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }
