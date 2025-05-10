from django.shortcuts import render, get_object_or_404, redirect
from controle_frota.models import TipoPlaca
from controle_frota.forms.editarTipoPlaca_forms import EditarTipoPlacaForm

def editar_tipoplaca_view(request, tipoplaca_id):
    tipo = get_object_or_404(TipoPlaca, pk=tipoplaca_id)
    if request.method == 'POST':
        form = EditarTipoPlacaForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_tipoplaca')
    else:
        form = EditarTipoPlacaForm(instance=tipo)
    return render(request, 'editar_tipoplaca.html', {'form': form})
