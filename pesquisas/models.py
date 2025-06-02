from django.db import models

class FamilyMember(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    escolaridade = models.CharField(max_length=255)
    ocupacao = models.CharField(max_length=255)
    rendimento = models.DecimalField(max_digits=10, decimal_places=2)
    portador_deficiencia = models.BooleanField()
    tipos_deficiencia = models.JSONField(blank=True, null=True)  # Store as JSON for multiple types

class QuestionarioSeharf(models.Model):
    # Personal Data
    nome = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=255)
    distrito = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    # Family Data
    membros_familia = models.ManyToManyField(FamilyMember, related_name="questionario_seharf")

    # Housing Conditions
    moradia_propria = models.BooleanField()
    titulo_propriedade = models.BooleanField(blank=True, null=True)
    possui_escritura = models.BooleanField(blank=True, null=True)
    outros_imoveis = models.IntegerField(blank=True, null=True)
    alugada = models.BooleanField(blank=True, null=True)
    terreno_construcao_alugada = models.BooleanField(blank=True, null=True)
    cedida = models.BooleanField(blank=True, null=True)
    terreno_construcao_cedida = models.BooleanField(blank=True, null=True)
    moradia_compartilhada = models.BooleanField(blank=True, null=True)
    estado_conservacao = models.CharField(max_length=50)
    tipo_construcao = models.CharField(max_length=50)
    num_quartos = models.IntegerField()
    num_banheiros = models.IntegerField()
    seguranca = models.JSONField(blank=True, null=True)
    tempo_deslocamento = models.CharField(max_length=50)

    # Neighborhood Infrastructure
    rua_pavimentacao = models.BooleanField()
    bairro_transporte_publico = models.BooleanField()
    rua_agua_tratada = models.BooleanField()
    rua_rede_esgoto = models.BooleanField()
    fossa_septica = models.BooleanField(blank=True, null=True)
    rua_rede_pluvial = models.BooleanField()
    bairro_area_lazer = models.BooleanField()
    bairro_escola = models.BooleanField()
    rua_rede_eletrica = models.BooleanField()
    rua_internet = models.BooleanField()
    bairro_creche = models.BooleanField()
    pavimentacao = models.CharField(max_length=50)
    gosta_bairro = models.BooleanField()
    onde_gostaria_morar = models.TextField(blank=True, null=True)
    melhor_bairro = models.TextField(blank=True, null=True)
    sonho = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created
