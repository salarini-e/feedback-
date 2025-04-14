#urlsp.py
from django.urls import path
from . import views

app_name = 'pesquisas'
urlpatterns = [
    path('', views.index, name='index'),
    path('questionario-seharf/', views.questionario_seharf, name='questionario_seharf'),
    # path('questionario_seharf/resultado', views.resultado, name='resultado'),
    # path('questionario_seharf/resultado/exportar', views.resultado_exportar, name='resultado_exportar'),
    path('questionario-seharf/exportar/', views.questionario_seharf_export_to_excel, name='questionario_seharf_export_to_excel'),
    #esboço
    path('sedarf/', views.esboco_pagina_sedarf, name='esboco'),
]
