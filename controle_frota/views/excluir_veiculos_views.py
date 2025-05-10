from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from controle_frota.models import Veiculo

@login_required
def excluir_veiculo_view(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')

    return render(request, 'excluir_veiculos.html', {'veiculo': veiculo})
