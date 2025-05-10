from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from controle_frota.models import GrupoVeiculo
from controle_frota.forms.excluirGrupoVeiculo_forms import ExcluirGrupoVeiculoForm

@login_required
def excluir_grupoveiculo_view(request, grupoveiculo_id):
    grupo = get_object_or_404(GrupoVeiculo, id=grupoveiculo_id)
    if request.method == 'POST':
        form = ExcluirGrupoVeiculoForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('confirmar'):
            grupo.delete()
            return redirect('cadastrar_grupoveiculo')
    else:
        form = ExcluirGrupoVeiculoForm()
    
    return render(request, 'excluir_grupoveiculo.html', {'form': form, 'grupo': grupo})
