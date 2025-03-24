from django import forms
from .models import Feedback

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
