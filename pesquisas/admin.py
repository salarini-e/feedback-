from django.contrib import admin
from .models import QuestionarioSeharf, FamilyMember as FamiliaMembro

# Customize the admin interface for QuestionarioSeharf
@admin.register(QuestionarioSeharf)
class QuestionarioSeharfAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cep', 'telefone', 'email', 'moradia_propria', 'gosta_bairro')
    search_fields = ('nome', 'cep', 'email', 'bairro', 'distrito')
    list_filter = ('moradia_propria', 'gosta_bairro', 'estado_conservacao', 'pavimentacao', 'created_at')
    ordering = ('-id',)
    filter_horizontal = ('membros_familia',)  # For ManyToManyField

# Customize the admin interface for FamiliaMembro
@admin.register(FamiliaMembro)
class FamiliaMembroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'escolaridade', 'ocupacao', 'rendimento', 'portador_deficiencia')
    search_fields = ('nome', 'escolaridade', 'ocupacao')
    list_filter = ('idade', 'rendimento', 'portador_deficiencia')
