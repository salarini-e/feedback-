from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg, Count
from .forms import FeedbackForm
from servicos.models import Local_de_atendimento
from .functions import get_feedback_distribution, get_frequencies, get_valores_termometro

def feedback(request, hash):
    local = get_object_or_404(Local_de_atendimento, hash=hash)
    if request.method == 'POST':
        print(request.POST)
        data = {
            'local': local.id,
            'ambiente': request.POST.get('ambiente'),
            'tempo_espera': request.POST.get('tempo'),
            'satisfacao': request.POST.get('satisfacao'),
            'atendimento': request.POST.get('atendimento'),
            'sugestoes': request.POST.get('sugestao'),
            'incluir_contato': bool(request.POST.get('resposta')),
        }
        if bool(request.POST.get('resposta')):
            data['contato_nome'] = request.POST.get('contato_nome')
            data['contato_telefoe'] = request.POST.get('contato_telefone')
        form = FeedbackForm(data)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.local = local
            feedback.save()                        
            return render(request, 'feedback_success.html', {'local': local})
        else:
            messages.error(request, "Por favor, corrija os erros no formulário.")
    else:
        form = FeedbackForm()

    context = {
        'local': local,
        'form': form
    }
    return render(request, 'feedback.html', context)

def painel_feedback(request, hash):
    local = get_object_or_404(Local_de_atendimento, hash=hash)
    feedbacks = local.feedbacks.all()    
    negative_feedbacks = feedbacks.filter(satisfacao__lt=3)
    feedbacks_with_suggestions = feedbacks.exclude(sugestoes__isnull=True).exclude(sugestoes__exact="").exclude(sugestoes__iexact="n/h")  # Exclui 'n/h'

    valores_satisfacao_geral = get_valores_termometro(feedbacks)
    summary = {
        
        'ambiente_dist': get_feedback_distribution(feedbacks, 'ambiente'),
        'tempo_espera_dist': get_feedback_distribution(feedbacks, 'tempo_espera'),
        'satisfacao_dist': get_feedback_distribution(feedbacks, 'satisfacao'),  
        'atendimento_dist': get_feedback_distribution(feedbacks, 'atendimento'),
        'total_feedbacks': feedbacks.count(),
        'negative_feedbacks': feedbacks.filter(satisfacao__lt=3).count(),
    }

    # Add moda and mediana to each metric
    contexto_estatisticas = {
        'ambiente': get_frequencies(feedbacks, 'ambiente'),
        'tempo_espera': get_frequencies(feedbacks, 'tempo_espera'),
        'satisfacao': get_frequencies(feedbacks, 'satisfacao'),
        'atendimento': get_frequencies(feedbacks, 'atendimento'),
    }

    summary_with_flags = [
        {
            'metric': key.replace('_dist', '').capitalize(),
            'is_distribution': key.endswith('_dist'),
            'data': value,
            'moda': contexto_estatisticas[key.replace('_dist', '')]['moda'],
            'mediana': contexto_estatisticas[key.replace('_dist', '')]['mediana']
        }
        for key, value in summary.items() if key.endswith('_dist')
    ]

    # Pass non-distribution keys separately
    non_distribution_summary = {
        'total_feedbacks': summary['total_feedbacks'],
        'negative_feedbacks': summary['negative_feedbacks'],
    }

    context = {
        'local': local,
        'feedbacks': feedbacks,
        'feedbacks_with_suggestions': feedbacks_with_suggestions,  # Atualizado para excluir 'n/h'
        'negative_feedbacks': negative_feedbacks,
        'summary': summary_with_flags,
        'non_distribution_summary': non_distribution_summary,
        'estatisticas': contexto_estatisticas,
        'valores_satisfacao_geral': valores_satisfacao_geral
    }

    if local.nome == 'SUBSECRETARIA DE TI':
        return render(request, 'painel_fedback_ti.html', context)
    return render(request, 'painel_fedback.html', context)