from django.urls import path
from . import views

app_name = 'servicos'
urlpatterns = [
    path('', views.list, name='index'),
    path('novo/', views.novo_atendimento, name='novo_atendimento'),
    path('editar/<hash>/', views.editar_atendimento, name='editar_atendimento'),
]