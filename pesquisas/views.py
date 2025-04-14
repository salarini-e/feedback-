from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import QuestionarioSeharf, FamilyMember
from .forms import QuestionnaireForm, FamilyMemberForm
import csv
from openpyxl import Workbook
from django.utils.timezone import make_naive
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('pesquisas:questionario_seharf')

def questionario_seharf(request):
    if request.method == 'POST':
        form_data = request.POST
        form_errors = {}

        # Validate required fields
        required_fields = ['nome', 'cep', 'rua', 'numero', 'bairro', 'distrito', 'telefone']
        for field in required_fields:
            if not form_data.get(field) or form_data.get(field).strip() == '':
                form_errors[field] = f"O campo {field} é obrigatório."

        # Additional validations (e.g., email format, numeric fields)
        if form_data.get('email') and '@' not in form_data['email']:
            form_errors['email'] = "Insira um email válido."

        if form_errors:
            return render(request, 'pesquisas/questionario_seharf.html', {
                'form_errors': form_errors,
                'request': request
            })

        # Save QuestionarioSeharf data
        questionario = QuestionarioSeharf.objects.create(
            nome=form_data.get('nome').strip(),
            cep=form_data.get('cep').strip(),
            rua=form_data.get('rua').strip(),
            numero=form_data.get('numero').strip(),
            bairro=form_data.get('bairro').strip(),
            distrito=form_data.get('distrito').strip(),
            telefone=form_data.get('telefone').strip(),
            email=form_data.get('email').strip() if form_data.get('email') else None,
            moradia_propria=form_data.get('moradia_propria') == 'sim',
            titulo_propriedade=form_data.get('titulo_propriedade') == 'sim',
            possui_escritura=form_data.get('possui_escritura') == 'sim',
            outros_imoveis=form_data.get('quantos_outros_imoveis') or None,
            alugada=form_data.get('alugada') == 'sim',
            terreno_construcao_alugada=form_data.get('terreno_construcao_alugada') == 'sim',
            cedida=form_data.get('cedida') == 'sim',
            terreno_construcao_cedida=form_data.get('terreno_construcao_cedida') == 'sim',
            moradia_compartilhada=form_data.get('moradia_compartilhada') == 'sim',
            estado_conservacao=form_data.get('estado_conservacao'),
            tipo_construcao=form_data.get('tipo_construcao'),
            num_quartos=form_data.get('num_quartos'),
            num_banheiros=form_data.get('num_banheiros'),
            seguranca=form_data.getlist('seguranca'),
            tempo_deslocamento=form_data.get('tempo_deslocamento'),
            rua_pavimentacao=form_data.get('rua_pavimentacao') == 'sim',
            bairro_transporte_publico=form_data.get('bairro_transporte_publico') == 'sim',
            rua_agua_tratada=form_data.get('rua_agua_tratada') == 'sim',
            rua_rede_esgoto=form_data.get('rua_rede_esgoto') == 'sim',
            fossa_septica=form_data.get('fossa_septica') == 'sim',
            rua_rede_fluvial=form_data.get('rua_rede_fluvial') == 'sim',
            bairro_area_lazer=form_data.get('bairro_area_lazer') == 'sim',
            bairro_escola=form_data.get('bairro_escola') == 'sim',
            rua_rede_eletrica=form_data.get('rua_rede_eletrica') == 'sim',
            rua_internet=form_data.get('rua_internet') == 'sim',
            bairro_creche=form_data.get('bairro_creche') == 'sim',
            pavimentacao=form_data.get('pavimentacao'),
            gosta_bairro=form_data.get('gosta_bairro') == 'sim',
            onde_gostaria_morar=form_data.get('onde_gostaria_morar'),
            melhor_bairro=form_data.get('melhor_bairro'),
            sonho=form_data.get('sonho')
        )

        # Save FamilyMember data
        family_members = []
        for key in form_data.keys():
            if key.startswith('familia_nome'):
                index = key.split('_')[-1]
                nome = form_data.get(f'familia_nome_{index}')
                if nome and nome.strip():  # Ensure the family member has a valid name
                    family_members.append(FamilyMember(
                        nome=nome.strip(),
                        idade=form_data.get(f'familia_idade_{index}'),
                        escolaridade=form_data.get(f'familia_escolaridade_{index}'),
                        ocupacao=form_data.get(f'familia_ocupacao_{index}'),
                        rendimento=form_data.get(f'familia_rendimento_{index}'),
                        portador_deficiencia=form_data.get(f'familia_deficiencia_{index}') == 'sim',
                        tipos_deficiencia=form_data.getlist(f'familia_deficiencia_tipo_{index}')
                    ))
        if family_members:
            FamilyMember.objects.bulk_create(family_members)

        # Link FamilyMember to QuestionarioSeharf
        questionario.membros_familia.set(FamilyMember.objects.filter(nome__in=[fm.nome for fm in family_members]))

        return HttpResponse("Formulário enviado com sucesso!")

    return render(request, 'pesquisas/questionario_seharf.html')

@login_required
def questionario_seharf_export_to_excel(request):
    # Create a workbook and a worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Questionário SEHARF"

    # Write the header row
    headers = [
        'ID', 'Nome', 'CEP', 'Rua', 'Número', 'Bairro', 'Distrito', 'Telefone', 'Email',
        'Moradia Própria', 'Título de Propriedade', 'Possui Escritura', 'Outros Imóveis',
        'Alugada', 'Terreno Construção Alugada', 'Cedida', 'Terreno Construção Cedida',
        'Moradia Compartilhada', 'Estado de Conservação', 'Tipo de Construção', 'Número de Quartos',
        'Número de Banheiros', 'Segurança', 'Tempo de Deslocamento', 'Rua Pavimentação',
        'Bairro Transporte Público', 'Rua Água Tratada', 'Rua Rede Esgoto', 'Fossa Séptica',
        'Rua Rede Fluvial', 'Bairro Área Lazer', 'Bairro Escola', 'Rua Rede Elétrica',
        'Rua Internet', 'Bairro Creche', 'Pavimentação', 'Gosta do Bairro', 'Onde Gostaria de Morar',
        'Melhor do Bairro', 'Sonho', 'Data de Criação'
    ]
    worksheet.append(headers)

    # Write data rows
    for questionario in QuestionarioSeharf.objects.all():
        worksheet.append([
            questionario.id, questionario.nome, questionario.cep, questionario.rua, questionario.numero,
            questionario.bairro, questionario.distrito, questionario.telefone, questionario.email,
            questionario.moradia_propria, questionario.titulo_propriedade, questionario.possui_escritura,
            questionario.outros_imoveis, questionario.alugada, questionario.terreno_construcao_alugada,
            questionario.cedida, questionario.terreno_construcao_cedida, questionario.moradia_compartilhada,
            questionario.estado_conservacao, questionario.tipo_construcao, questionario.num_quartos,
            questionario.num_banheiros, ', '.join(questionario.seguranca or []), questionario.tempo_deslocamento,
            questionario.rua_pavimentacao, questionario.bairro_transporte_publico, questionario.rua_agua_tratada,
            questionario.rua_rede_esgoto, questionario.fossa_septica, questionario.rua_rede_fluvial,
            questionario.bairro_area_lazer, questionario.bairro_escola, questionario.rua_rede_eletrica,
            questionario.rua_internet, questionario.bairro_creche, questionario.pavimentacao,
            questionario.gosta_bairro, questionario.onde_gostaria_morar, questionario.melhor_bairro,
            questionario.sonho, make_naive(questionario.created_at)  # Convert to naive datetime
        ])

    # Prepare the response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="questionario_seharf.xlsx"'

    # Save the workbook to the response
    workbook.save(response)
    return response

def esboco_pagina_sedarf(request):
    return render(request, 'pesquisas/esboco_pagina_sedarf.html')