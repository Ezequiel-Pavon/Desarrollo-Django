from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


#(request) es una solicitud

def inicio(request):
    return HttpResponse("<h1>Bienvenido!!</h1>") #imprime un texto html


def turnos(request):
    return render(request, 'paginas/turnos.html')
