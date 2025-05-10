from django import forms
from controle_frota.models import TipoPlaca

class CadastrarTipoPlacaForm(forms.ModelForm):
    class Meta:
        model = TipoPlaca
        fields = ['nome']
