from django.shortcuts import render
from servicos.models import Local_de_atendimento

def feedback(request, hash):
    local = Local_de_atendimento.objects.get(hash=hash)
    if request.method == 'POST':
        print(request.POST)
    context = {
        'local': local
    }
    return render(request, 'feedback.html', context)