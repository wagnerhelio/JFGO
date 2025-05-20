from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from controle_frota.models import Veiculo

@login_required
def menu_view(request):

    total = Veiculo.objects.count()
    ativos = Veiculo.objects.filter(ativo=True).count()
    inativos = Veiculo.objects.filter(ativo=False).count()

    return render(request, 'menu.html', {
        'total': total,
        'ativos': ativos,
        'inativos': inativos,
    })
