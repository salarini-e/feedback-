# Generated by Django 5.1.7 on 2025-05-30 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
        ('servicos', '0004_local_de_atendimento_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesquisaSatisfacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('internet_item1', models.IntegerField()),
                ('internet_item2', models.IntegerField()),
                ('internet_item3', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('internet_item4', models.IntegerField()),
                ('telefonia_item1', models.IntegerField()),
                ('telefonia_item2', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('telefonia_item3', models.IntegerField()),
                ('suporte_item4', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('telefonia_item5', models.IntegerField()),
                ('impressora_item1', models.IntegerField()),
                ('impressora_item2', models.IntegerField()),
                ('impressora_item3', models.IntegerField()),
                ('impressora_item4', models.IntegerField()),
                ('impressora_item5', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('sistema_gestao_item2', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('sistema_gestao_item3', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3)),
                ('sistema_gestao_item4', models.IntegerField()),
                ('sistema_gestao_item5', models.IntegerField()),
                ('processo_item1', models.IntegerField()),
                ('processo_item2', models.IntegerField()),
                ('processo_item3', models.IntegerField()),
                ('tramitacao_item1', models.IntegerField()),
                ('tramitacao_item2', models.IntegerField()),
                ('tramitacao_item3', models.IntegerField()),
                ('tramitacao_item4', models.IntegerField()),
                ('suporte_item1', models.IntegerField()),
                ('suporte_item2', models.IntegerField()),
                ('suporte_item3', models.IntegerField()),
                ('resposta', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3, null=True)),
                ('contato_nome', models.CharField(blank=True, max_length=255, null=True)),
                ('contato_telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesquisas', to='servicos.local_de_atendimento')),
            ],
        ),
    ]
