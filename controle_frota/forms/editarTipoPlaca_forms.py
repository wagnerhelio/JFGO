from django import forms
from controle_frota.models import TipoPlaca

class EditarTipoPlacaForm(forms.ModelForm):
    class Meta:
        model = TipoPlaca
        fields = ['nome']
