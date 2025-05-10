from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from controle_frota.forms.cadastrarVeiculos_forms import CadastrarVeiculosForm

@login_required
def cadastrar_veiculos_views(request):
    if request.method == 'POST':
        form = CadastrarVeiculosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = CadastrarVeiculosForm()
    return render(request, 'cadastrar_veiculos.html', {'form': form})