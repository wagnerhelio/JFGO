from django.contrib import admin
from controle_frota.models import Veiculo, TipoPlaca, GrupoVeiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'marca', 'ano_fabricacao', 'cor', 'tipo_placa', 'grupo', 'ativo')
    search_fields = ('placa', 'modelo', 'chassi', 'numero_motor')
    list_filter = ('ativo', 'tipo_placa', 'grupo', 'marca', 'cor')

admin.site.register(TipoPlaca)
admin.site.register(GrupoVeiculo)    