from django.contrib import admin
from website.models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('opcao', 'comentario', 'data_de_envio')  # Campos a exibir na lista
    list_filter = ('opcao', 'data_de_envio')  # Filtros rápidos
    search_fields = ('comentario',)  # Campos pesquisáveis
    ordering = ('data_de_envio',)  # Ordenação por data, mais recentes primeiro

admin.site.register(Avaliacao, AvaliacaoAdmin)
