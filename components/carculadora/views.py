from django.shortcuts import render

def carculadora(request):
    context = {}
    return render(request, 'carculadora/carculadora.html', context)

