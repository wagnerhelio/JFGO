from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from controle_frota.models import Requisicao
from controle_frota.forms.editarStatusRequisicao_forms import EditarStatusRequisicaoForm

@login_required
def editar_status_requisicao_view(request, requisicao_id):
    requisicao = get_object_or_404(Requisicao, pk=requisicao_id)

    if request.method == 'POST':
        form = EditarStatusRequisicaoForm(request.POST, instance=requisicao)
        if form.is_valid():
            form.save()
            return redirect('listar_requisicao')
    else:
        form = EditarStatusRequisicaoForm(instance=requisicao)

    return render(request, 'editar_status_requisicao.html', {'form': form, 'requisicao': requisicao})
