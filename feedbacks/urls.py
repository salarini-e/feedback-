from django.urls import path
from . import views

app_name = 'feedbacks'
urlpatterns = [
    # Example URL patterns
    # path('', views.index, name='index'),
    path('<hash>/', views.feedback, name='feedback'),
    path('painel/<hash>/', views.painel_feedback, name='painel_feedback'),
]