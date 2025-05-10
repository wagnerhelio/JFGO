from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect

from controle_frota.views.login_views import login_ad_view, logout_view
from controle_frota.views.menu_views import menu_view
from controle_frota.views.cadastrar_veiculos_views import cadastrar_veiculos_views
from controle_frota.views.listar_veiculos_views import listar_veiculos_views
from controle_frota.views.editar_veiculos_views import editar_veiculo_view
from controle_frota.views.excluir_veiculos_views import excluir_veiculo_view
from controle_frota.views.cadastrar_tipoplaca_views import cadastrar_tipoplaca_view
from controle_frota.views.cadastrar_grupoveiculo_views import cadastrar_grupoveiculo_view
from controle_frota.views.logout_view import logout_view
from controle_frota.views.editar_tipoplaca_views import editar_tipoplaca_view
from controle_frota.views.excluir_tipoplaca_views import excluir_tipoplaca_view
from controle_frota.views.editar_grupoveiculo_views import editar_grupoveiculo_view
from controle_frota.views.excluir_grupoveiculo_views import excluir_grupoveiculo_view

urlpatterns = [
    # Redirecionamento raiz para login
    path('', lambda request: redirect('login')),

    # Autenticação
    path('login/', login_ad_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Admin Django
    path('admin/', admin.site.urls),

    # Menu principal
    path('menu/', menu_view, name='menu'),

    # Veículos
    path('cadastrar/', cadastrar_veiculos_views, name='cadastrar_veiculos'),
    path('listar/', listar_veiculos_views, name='listar_veiculos'),
    path('editar/<int:veiculo_id>/', editar_veiculo_view, name='editar_veiculo'),
    path('excluir/<int:veiculo_id>/', excluir_veiculo_view, name='excluir_veiculo'),

    # Cadastros tipoplaca
    path('cadastrar_tipoplaca/', cadastrar_tipoplaca_view, name='cadastrar_tipoplaca'),
    path('tipoplaca/editar/<int:tipoplaca_id>/', editar_tipoplaca_view, name='editar_tipoplaca'),
    path('tipoplaca/excluir/<int:tipoplaca_id>/', excluir_tipoplaca_view, name='excluir_tipoplaca'),
    
    # Cadastros grupoveiculo
    path('cadastrar_grupoveiculo/', cadastrar_grupoveiculo_view, name='cadastrar_grupoveiculo'),
    path('editar_grupoveiculo/<int:grupoveiculo_id>/', editar_grupoveiculo_view, name='editar_grupoveiculo'),
    path('excluir_grupoveiculo/<int:grupoveiculo_id>/', excluir_grupoveiculo_view, name='excluir_grupoveiculo'),
]
