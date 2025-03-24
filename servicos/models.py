from django.db import models

# Create your models here.

class Local_de_atendimento(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=32, blank=True, null=True)    
    def __str__(self):
        return self.nome

    def gerar_hash(self):
        import hashlib
        import time
        import random
        hash = hashlib.md5()
        hash.update(str(time.time()).encode())
        hash.update(str(random.randint(1, 1000)).encode())
        self.hash = hash.hexdigest()
        self.save()

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        if not self.hash:
            self.gerar_hash()
        super(Local_de_atendimento, self).save(*args, **kwargs)