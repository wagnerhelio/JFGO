from django.contrib import admin
from controle_frota.models import Veiculo, TipoPlaca, GrupoVeiculo,Requisicao

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'marca', 'ano_fabricacao', 'cor', 'tipo_placa', 'grupo', 'ativo')
    search_fields = ('placa', 'modelo', 'chassi', 'numero_motor')
    list_filter = ('ativo', 'tipo_placa', 'grupo', 'marca', 'cor')

admin.site.register(TipoPlaca)
admin.site.register(GrupoVeiculo)    

@admin.register(Requisicao)
class RequisicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'veiculo', 'data_utilizacao', 'unidade')
    list_filter = ('tipo', 'data_utilizacao', 'unidade')
    search_fields = ('veiculo__placa', 'unidade', 'usuario', 'itinerario')
