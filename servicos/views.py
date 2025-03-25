from django.shortcuts import render, redirect, get_object_or_404
from .models import Local_de_atendimento
from .forms import LocalDeAtendimentoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list(request):
    context = {
        'locais': Local_de_atendimento.objects.all()
    }
    return render(request, 'list.html', context)

@login_required
def novo_atendimento(request):
    if not request.user.is_superuser:
        return redirect('servicos:index')
    
    if request.method == 'POST':
        form = LocalDeAtendimentoForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('servicos:index')  # Redireciona para a página inicial após salvar
    else:
        form = LocalDeAtendimentoForm()
    return render(request, 'novo_atendimento.html', {'form': form})

@login_required
def editar_atendimento(request, hash):
    if not request.user.is_superuser:
        return redirect('servicos:index')    
    local = get_object_or_404(Local_de_atendimento, hash=hash)
    if request.method == 'POST':
        form = LocalDeAtendimentoForm(request.POST, request.FILES, instance=local)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('servicos:index')  # Redireciona para a página inicial após salvar
    else:
        form = LocalDeAtendimentoForm(instance=local)
    return render(request, 'editar_atendimento.html', {'form': form})