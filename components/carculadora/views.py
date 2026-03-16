from django.shortcuts import render

def carculadora(request):
    context = {}
    
    if request.method == "POST":
        # Capturamos los datos del formulario
        try:
            num1 = int(request.POST.get('num1', 0))
            num2 = int(request.POST.get('num2', 0))
            operacion = request.POST.get('operacion')
            resultado = 0

            # Lógica aritmética
            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multi':
                resultado = num1 * num2
            elif operacion == 'divi':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error (Div/0)"
            
            # Formateamos el resultado para evitar demasiados decimales
            if isinstance(resultado, int):
                resultado = round(resultado, 2)

            # Enviamos el resultado y los números de vuelta para que no se borren de los inputs
            context = {
                'resultado': resultado,
                'num1': num1,
                'num2': num2
            }
            
        except ValueError:
            context = {'resultado': "Entrada inválida"}

    return render(request, 'carculadora/carculadora.html', context)