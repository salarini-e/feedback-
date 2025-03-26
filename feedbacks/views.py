from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg, Count
from .forms import FeedbackForm
from servicos.models import Local_de_atendimento

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
    summary = {
        'avg_satisfaction': feedbacks.aggregate(Avg('satisfacao'))['satisfacao__avg'],
        'avg_ambiente': feedbacks.aggregate(Avg('ambiente'))['ambiente__avg'],
        'avg_tempo_espera': feedbacks.aggregate(Avg('tempo_espera'))['tempo_espera__avg'],
        'avg_atendimento': feedbacks.aggregate(Avg('atendimento'))['atendimento__avg'],
        'total_feedbacks': feedbacks.count(),
        'negative_feedbacks': negative_feedbacks.count(),
    }
    context = {
        'local': local,
        'feedbacks': feedbacks,
        'negative_feedbacks': negative_feedbacks,
        'summary': summary,
    }

    if local.nome == 'SUBSECRETARIA DE TI':
        return render(request, 'painel_fedback_ti.html', context)
    return render(request, 'painel_fedback.html', context)