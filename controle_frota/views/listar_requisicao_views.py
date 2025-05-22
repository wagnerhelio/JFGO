from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from controle_frota.models import Requisicao

@login_required
def listar_requisicao_view(request):
    requisicoes = Requisicao.objects.all().order_by('-data_utilizacao')

    context = {
        'requisicoes': requisicoes
    }
    
    return render(request, 'listar_requisicao.html', context)
