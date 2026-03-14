from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def todolist(request):
    template = loader.get_template('todolist/to_do_list.html')
    context = {}
    return HttpResponse(template.render(context,request))