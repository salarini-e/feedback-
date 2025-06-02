from django import forms
from .models import Feedback, PesquisaSatisfacao

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'ambiente', 'tempo_espera', 'satisfacao', 'atendimento', 
            'sugestoes', 'incluir_contato', 'contato_nome', 'contato_telefoe'
        ]
        widgets = {
            'sugestoes': forms.Textarea(attrs={'rows': 4}),
            'contato_nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'contato_telefoe': forms.TextInput(attrs={'placeholder': 'Seu telefone'}),
        }

class PesquisaSatisfacaoForm(forms.ModelForm):
    class Meta:
        model = PesquisaSatisfacao
        fields = '__all__'
        widgets = {
            'internet_item3': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'telefonia_item2': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'suporte_item4': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'impressora_item5': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'sistema_gestao_item2': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'sistema_gestao_item3': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
            'resposta': forms.RadioSelect(choices=[('sim', 'Sim'), ('nao', 'Não')]),
        }

