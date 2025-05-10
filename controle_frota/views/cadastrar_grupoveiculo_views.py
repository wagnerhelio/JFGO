from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from controle_frota.forms.cadastrarGrupoVeiculo_forms import CadastrarGrupoVeiculoForm
from controle_frota.models.grupoVeiculo_models import GrupoVeiculo

@login_required
def cadastrar_grupoveiculo_view(request):
    form = CadastrarGrupoVeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastrar_grupoveiculo')  # redireciona para a mesma página
    grupos = GrupoVeiculo.objects.all()
    return render(request, 'cadastrar_grupoveiculo.html', {
        'form': form,
        'grupos': grupos
    })
