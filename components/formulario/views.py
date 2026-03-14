from django.shortcuts import render

def formulario(request):
    context = {}
    return render(request, 'formulario/formulario.html', context)