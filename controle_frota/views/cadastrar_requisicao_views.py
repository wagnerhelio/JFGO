from django.shortcuts import render, redirect
from controle_frota.forms.cadastrarRequisicao_forms import CadastrarRequisicaoForm
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_requisicao_view(request):
    form = CadastrarRequisicaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_requisicao')
    return render(request, 'cadastrar_requisicao.html', {'form': form})
