from django.urls import path
from . import views

urlpatterns = [
    path('total_letras/', views.contar_letras, name='contletras_letras'),
]