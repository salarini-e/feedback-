from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),  # Add this line for the login view
    path('logout/', views.logout, name='logout'),  # Add this line for the logout view
]