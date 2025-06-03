#urlsp.py
from django.urls import path
from . import views

app_name = 'botwhatsapp'
urlpatterns = [
    path('avaliacoes-atendimento-whatsapp/', views.avaliacoes_atendimento_whatsapp, name='avaliacoes_atendimento_whatsapp'),
    path('avaliacoes-atendimento-whatsapp/exportar/', views.avaliacoes_atendimento_whatsapp_exportar, name='avaliacoes_atendimento_whatsapp_exportar'),
]
