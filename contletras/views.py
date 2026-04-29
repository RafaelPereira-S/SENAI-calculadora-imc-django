from django.shortcuts import render



def contar_letras(request):

    total_letters = None
    palavra = ' '

    if request.method == "POST":

        palavra = request.POST.get('palavra', ' ').strip()

        total_letters = len(palavra)

    return render(request, 'contletras/index.html',

        {
            'total_letters': total_letters,
            'palavra' : palavra
        })