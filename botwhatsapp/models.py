from django.db import models

# Create your models here.
class AvaliacaoAtendimento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=15)
    avaliacao = models.IntegerField(choices=[(1, '1 - Satisfeito'), (2, '2 - Regular'), (3, '3 - Insatisfeito')])

    def __str__(self):
        return f"{self.telefone} - {self.avaliacao} - {self.data.strftime('%Y-%m-%d %H:%M:%S')}"