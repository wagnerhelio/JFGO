from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from controle_frota.models import Veiculo
from controle_frota.forms.editarVeiculos_forms import EditarVeiculosForm

@login_required
def editar_veiculo_view(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == 'POST':
        form = EditarVeiculosForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = EditarVeiculosForm(instance=veiculo)

    return render(request, 'editar_veiculos.html', {'form': form, 'veiculo': veiculo})
