from django.contrib import admin
from .models import AvaliacaoAtendimento

# Register your models here.
class AvaliacaoAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'telefone', 'avaliacao')
    list_filter = ('avaliacao',)
    search_fields = ('telefone',)

admin.site.register(AvaliacaoAtendimento, AvaliacaoAtendimentoAdmin)