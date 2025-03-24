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

    def get_ambiente_icon(self):
        return self._get_icon(self.ambiente)

    def get_tempo_espera_icon(self):
        return self._get_icon(self.tempo_espera)

    def get_satisfacao_icon(self):
        return self._get_icon(self.satisfacao)

    def get_atendimento_icon(self):
        return self._get_icon(self.atendimento)

    def _get_icon(self, value):
        icons = {
            1: {"icon": "fa-face-angry", "color": "red"},
            2: {"icon": "fa-face-frown", "color": "orange"},
            3: {"icon": "fa-face-meh", "color": "rgb(235, 219, 0)"},
            4: {"icon": "fa-face-smile-beam", "color": "rgb(61, 212, 61)"},
            5: {"icon": "fa-face-grin-wink", "color": "green"},
        }
        return icons.get(value, {"icon": "fa-question-circle", "color": "black"})

    def has_negative_feedback(self):
        return any(
            rating <= 3 for rating in [
                self.ambiente,
                self.tempo_espera,
                self.satisfacao,
                self.atendimento
            ]
        )
