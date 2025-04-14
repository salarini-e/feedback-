from django import forms
from .models import QuestionarioSeharf, FamilyMember

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['nome', 'idade', 'escolaridade', 'ocupacao', 'rendimento', 'portador_deficiencia', 'tipos_deficiencia']

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionarioSeharf
        exclude = ['membros_familia']  # Exclude family members to handle separately
