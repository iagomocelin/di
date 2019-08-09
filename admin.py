from django.contrib import admin

# Register your models here.
from planodeacao.models import Perspectiva , ObjetivoEstrategico , AcoesOrcamentarias , NaturezadeDespesa , AquisicoesOrcamentarias

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

class AdminAquisicoesOrcamentarias(admin.ModelAdmin):
    list_display = ( 'descricaodaaquisicao' ,)
    list_filter = ( 'descricaodaaquisicao' ,)


admin.site.register(Perspectiva, AdminPerspectiva)
admin.site.register(ObjetivoEstrategico, AdminObjetivoEstrategico)
admin.site.register(AcoesOrcamentarias, AdminAcoesOrcamentarias)
admin.site.register(NaturezadeDespesa, AdminNaturezadeDespesa)
admin.site.register(AquisicoesOrcamentarias, AdminAquisicoesOrcamentarias)