from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from controle_frota.models import GrupoVeiculo
from controle_frota.forms.editarGrupoVeiculo_forms import EditarGrupoVeiculoForm

@login_required
def editar_grupoveiculo_view(request, grupoveiculo_id):
    grupo = get_object_or_404(GrupoVeiculo, id=grupoveiculo_id)
    form = EditarGrupoVeiculoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('cadastrar_grupoveiculo')
    return render(request, 'editar_grupoveiculo.html', {'form': form, 'grupo': grupo})