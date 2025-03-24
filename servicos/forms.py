from django import forms
from .models import Local_de_atendimento

class LocalDeAtendimentoForm(forms.ModelForm):
    class Meta:
        model = Local_de_atendimento
        fields = ['nome', 'descricao','endereco']