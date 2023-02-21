from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path('tests/', views.test_covid, name='tests'),
    path('busqueda-profesional/', views.busqueda_profesional, name='busqueda-profesional'),
    path('buscar/', views.buscar, name='buscar')
]