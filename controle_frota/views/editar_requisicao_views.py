from django.shortcuts import render, redirect, get_object_or_404
from controle_frota.models import Requisicao
from controle_frota.forms.editarRequisicao_forms import EditarRequisicaoForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_requisicao_view(request, requisicao_id):
    requisicao = get_object_or_404(Requisicao, id=requisicao_id)
    form = EditarRequisicaoForm(request.POST or None, instance=requisicao)
    if form.is_valid():
        form.save()
        return redirect('listar_requisicao')
    return render(request, 'editar_requisicao.html', {'form': form, 'requisicao': requisicao})
