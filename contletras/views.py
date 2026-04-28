from django.shortcuts import render

# def contar_letras(request):
#     # Inicializamos a variável como None ou 0 para evitar erro de "variável não definida"
#     letras_contadas = None 

#     if request.method == "POST":
#         # Pegamos o valor do input (certifique-se que o 'name' no HTML é 'palavra')
#         palavra = request.POST.get('palavra', '')

#         # Em Python, para contar caracteres, basta usar len()
#         # Não é necessário fazer um loop 'for' para isso
#         letras_contadas = len(palavra)
        
#     return render(request, 'contletras/index.html', {
#         'total_letras': letras_contadas
#     })


def contar_letras(request,):

    total_letters: None

    if request.method == "POST":

        palavra = str(request.POST.get('palavra'))
        for i in range(len(palavra)):

            i += 1

            letras_contadas = i

    return render(request, 'contletras/index.html',

        {

            'total_letras': letras_contadas

        })

