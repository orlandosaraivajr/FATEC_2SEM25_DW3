from django.contrib import admin
from core.models import FeriadoModel
from datetime import datetime

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia', 'mes', 'modificado_em', 'registro_no_mes')
    list_filter = ('mes',)
    search_fields = ('nome',)
    ordering = ('mes', 'dia')
    readonly_fields = ('modificado_em',)
    
    def registro_no_mes(self, obj):
        hoje = datetime.now()
        return obj.mes == hoje.month
    
    registro_no_mes.short_description = 'Feriado neste mês?'
    registro_no_mes.boolean = True

admin.site.register(FeriadoModel, FeriadoModelAdmin)
