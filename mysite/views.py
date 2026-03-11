from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hola Mundo</h1> <br> <p>Bienvenido a Django</p> <br> <div> <h2>Características de Django</h2> <ul> <li>Aprende Django</li> <li>Construye proyectos</li> <li>Comparte tu conocimiento</li> </ul> </div>")
