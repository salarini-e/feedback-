from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    return redirect('servicos:index')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('servicos:index')  # Redirect to a desired page after login
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})  # Add error message
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout