from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
    path('pagina1/', views.texto01, name='Página 01'),
    path('pagina2/', views.texto02, name='Página 02'),
    path('pagina3/', views.texto03, name='Página 03'),
    path('pagina4/', views.texto04, name='Página 04'),
]