from django.shortcuts import render, get_object_or_404, redirect
from controle_frota.models import TipoPlaca

def excluir_tipoplaca_view(request, tipoplaca_id):
    tipo = get_object_or_404(TipoPlaca, pk=tipoplaca_id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('cadastrar_tipoplaca')
    return render(request, 'excluir_tipoplaca.html', {'tipo': tipo})
