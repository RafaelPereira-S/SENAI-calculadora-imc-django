from django.shortcuts import render

# Create your views here.

def somar(request,num1,num2):
    resultado = None
    if request.method == 'POST':
        num1 = int(request.POST.get(   ))  #---> Não esquecer de adicionar a função
