from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from controle_frota.models import Veiculo 
from controle_frota.forms.listarVeiculos_forms import ListarVeiculosForm

@login_required
def listar_veiculos_views(request):
    form = ListarVeiculosForm(request.GET or None)
    veiculos = Veiculo.objects.all()

    if form.is_valid():
        if form.cleaned_data['grupo']:
            veiculos = veiculos.filter(grupo=form.cleaned_data['grupo'])
        if form.cleaned_data['tipo_placa']:
            veiculos = veiculos.filter(tipo_placa=form.cleaned_data['tipo_placa'])
        if form.cleaned_data['placa']:
            veiculos = veiculos.filter(placa__icontains=form.cleaned_data['placa'])

    return render(request, 'listar_veiculos.html', {'form': form, 'veiculos': veiculos})
