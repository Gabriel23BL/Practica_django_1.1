from django.shortcuts import render

def todolist(request):
    context = {}
    return render(request, 'todolist/to_do_list.html', context)