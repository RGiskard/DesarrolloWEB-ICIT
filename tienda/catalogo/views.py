from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
body = '''
    <!DOCTYPE html>
    <html>
        <body>
            <h1>My First Heading</h1>
            <p>My first paragraph.</p>
        </body>
    </html> 
    '''

dummyBody = "Hello World"

def Home(request):
    return HttpResponse(body)
    #return "Hello World"

def Home2(request):
    return HttpResponse("Hello World 2")

def Home3(request):
    saludo = "Hola mundo template"
    cuerpo = "<h1>Texto HTML</h1>"
    ctx = {
        'saludo':saludo,
        'cuerpo':cuerpo,
    }
    return render(request,'catalogo/visualizar.html',ctx)