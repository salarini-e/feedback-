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


class PesquisaSatisfacao(models.Model):
    local = models.ForeignKey(Local_de_atendimento, on_delete=models.CASCADE, related_name='pesquisas', null=True, blank=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    
    internet_item1 = models.IntegerField()
    internet_item2 = models.IntegerField()
    internet_item3 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    internet_item3_porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo")
    internet_item4 = models.IntegerField()
    internet_item5 = models.IntegerField()    

    telefonia_item1 = models.IntegerField()
    telefonia_item2 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    telefonia_item2_porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo")
    telefonia_item3 = models.IntegerField()
    suporte_item4 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], verbose_name="Telefonia Item 4")
    suporte_item4_porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo", verbose_name="Telefonia Item 4")
    telefonia_item5 = models.IntegerField()
    telefonia_item6 = models.IntegerField()

    impressora_item1 = models.IntegerField()
    impressora_item2 = models.IntegerField()
    impressora_item3 = models.IntegerField()
    impressora_item4 = models.IntegerField()
    impressora_item5 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    impressora_item5_porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo")
    impressora_item6 = models.IntegerField()

    CHOICES_SISTEMA = [
        ('pro', 'Protocolo'),
        ('gma', 'GMA'),
        ('tri', 'Tributário'),
        ('out', 'Outro'),
        ('n/a', 'Não se aplica')        
    ]
    sistema_gestao_item1 = models.CharField(max_length=3, choices=CHOICES_SISTEMA, default='n/a')
    sistema_gestao_item2 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    sistema_gestao_item2_porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo")
    sistema_gestao_item3 = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    sistema_gestao_item3porque = models.CharField(max_length=255, blank=True, null=True, help_text="Se 'Não', explique o motivo")
    sistema_gestao_item4 = models.IntegerField()
    sistema_gestao_item5 = models.IntegerField()

    processo_item1 = models.IntegerField()
    processo_item2 = models.IntegerField()
    processo_item3 = models.IntegerField()

    tramitacao_item1 = models.IntegerField()
    tramitacao_item2 = models.IntegerField()
    tramitacao_item3 = models.IntegerField()
    tramitacao_item4 = models.IntegerField()

    suporte_item1 = models.IntegerField()
    suporte_item2 = models.IntegerField()
    suporte_item3 = models.IntegerField()
    suporte_item4 = models.IntegerField()
    
    resposta = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], blank=True, null=True)    
    contato_nome = models.CharField(max_length=255, blank=True, null=True)
    contato_telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Pesquisa {self.id} - {self.local.nome}"
