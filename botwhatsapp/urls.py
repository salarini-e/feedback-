#urlsp.py
from django.urls import path
from . import views

app_name = 'botwhatsapp'
urlpatterns = [
    path('avaliacoes-atendimento/', views.avaliacoes_atendimento_whatsapp, name='avaliacoes_atendimento_whatsapp'),
    path('avaliacoes-atendimento/exportar/', views.avaliacoes_atendimento_whatsapp_exportar, name='avaliacoes_atendimento_whatsapp_exportar'),
]
