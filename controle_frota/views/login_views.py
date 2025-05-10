from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_ad_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Verifica de qual backend o usuário foi autenticado
            backend_path = getattr(user, 'backend', '')
            if 'ldap_backend' in backend_path.lower():
                tipo_usuario = 'usuário LDAP'
            else:
                tipo_usuario = 'usuário local'

            messages.success(request, f'Bem-vindo, {username}! ({tipo_usuario})')
            return redirect('menu')
        else:
            messages.error(request, 'Usuário ou senha inválidos, ou falha na autenticação do AD.')
    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')