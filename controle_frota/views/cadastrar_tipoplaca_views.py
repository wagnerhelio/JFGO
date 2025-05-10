from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from controle_frota.forms.cadastrarTipoPlaca_forms import CadastrarTipoPlacaForm
from controle_frota.models import TipoPlaca  # IMPORTANTE

@login_required
def cadastrar_tipoplaca_view(request):
    form = CadastrarTipoPlacaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastrar_tipoplaca')  # Redireciona para mesma tela para atualizar a lista

    tipos = TipoPlaca.objects.all().order_by('nome')  # BUSCA OS TIPOS CADASTRADOS

    return render(request, 'cadastrar_tipoplaca.html', {
        'form': form,
        'tipos': tipos  # PASSA A LISTA PARA O TEMPLATE
    })
