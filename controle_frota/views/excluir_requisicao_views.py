from django.shortcuts import render, redirect, get_object_or_404
from controle_frota.models import Requisicao
from controle_frota.forms.excluirRequisicao_forms import ExcluirRequisicaoForm
from django.contrib.auth.decorators import login_required

@login_required
def excluir_requisicao_view(request, requisicao_id):
    requisicao = get_object_or_404(Requisicao, id=requisicao_id)
    if request.method == 'POST':
        form = ExcluirRequisicaoForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmar']:
            requisicao.delete()
            return redirect('listar_requisicao')
    else:
        form = ExcluirRequisicaoForm()
    return render(request, 'excluir_requisicao.html', {'form': form, 'requisicao': requisicao})
