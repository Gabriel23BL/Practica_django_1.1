from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'home/home.html', context)


#Otra forma de importarn las views
#from django.http import HttpResponse
#from django.shortcuts import render
#from django.template import loader

#def index(request):
    #template = loader.get_template('home/home.html')
    #context = {}
    #return HttpResponse(template.render(context,request))