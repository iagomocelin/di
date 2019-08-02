from django.contrib import admin

from planodeacao.models import Perspectiva , ObjetivoEstrategico , AcoesOrcamentarias , NaturezadeDespesa

class AdminPerspectiva(admin.ModelAdmin):
    list_display = ( 'descricao' ,)
    list_filter = ( 'descricao' ,)

class AdminObjetivoEstrategico(admin.ModelAdmin):
    list_display = ( 'descricao' ,)
    list_filter = ( 'descricao' ,)

class AdminAcoesOrcamentarias(admin.ModelAdmin):
    list_display = ( 'descricao' ,)
    list_filter = ( 'descricao' ,)

class AdminNaturezadeDespesa(admin.ModelAdmin):
    list_display = ( 'rubrica' ,)
    list_filter = ( 'rubrica' ,)

admin.site.register(Perspectiva, AdminPerspectiva)
admin.site.register(ObjetivoEstrategico, AdminObjetivoEstrategico)
admin.site.register(AcoesOrcamentarias, AdminAcoesOrcamentarias)
admin.site.register(NaturezadeDespesa, AdminNaturezadeDespesa)