from django.contrib import admin
from .models import Feedback

# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'local', 'dt_inclusao', 'ambiente', 'tempo_espera', 'satisfacao', 'atendimento', 'incluir_contato')
    list_filter = ('local', 'dt_inclusao', 'satisfacao', 'atendimento')
    search_fields = ('local__nome', 'contato_nome', 'contato_telefoe')
    ordering = ('-dt_inclusao',)
