from django.db import models

# Create your models here.
from django.db import models
from servicos.models import Local_de_atendimento

class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Notas de 1 a 5
    
    local = models.ForeignKey(Local_de_atendimento, on_delete=models.CASCADE, related_name='feedbacks')
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ambiente = models.IntegerField(choices=RATING_CHOICES)
    tempo_espera = models.IntegerField(choices=RATING_CHOICES)
    satisfacao = models.IntegerField(choices=RATING_CHOICES)
    atendimento = models.IntegerField(choices=RATING_CHOICES)
    sugestoes = models.TextField(blank=True, null=True)
    incluir_contato = models.BooleanField(default=False)
    contato_nome = models.CharField(max_length=255, blank=True, null=True, help_text="Opcional")
    contato_telefoe = models.CharField(max_length=20, blank=True, null=True, help_text="Opcional")
    
    def __str__(self):
        return f"Feedback {self.id} - {self.local.nome}"
