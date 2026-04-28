from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
    path('pagina1/', views.calcular_imc, name='calculadora_imc'),
    path('pagina2/', views.calcular_imc, name='calculadora_imc'),
]