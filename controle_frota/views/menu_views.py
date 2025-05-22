from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from controle_frota.models import Veiculo, Requisicao

@login_required
def menu_view(request):
    # KPIs de Veículos
    total = Veiculo.objects.count()
    ativos = Veiculo.objects.filter(ativo=True).count()
    inativos = Veiculo.objects.filter(ativo=False).count()

    # KPIs de Requisições
    total_requisicoes = Requisicao.objects.count()
    requisicoes_pendentes = Requisicao.objects.filter(status='Pendente').count()
    requisicoes_aprovadas = Requisicao.objects.filter(status='Aprovada').count()

    context = {
        'total': total,
        'ativos': ativos,
        'inativos': inativos,
        'total_requisicoes': total_requisicoes,
        'requisicoes_pendentes': requisicoes_pendentes,
        'requisicoes_aprovadas': requisicoes_aprovadas,
    }

    return render(request, 'menu.html', context)
