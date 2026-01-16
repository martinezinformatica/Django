#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def hello(request): 
    return HttpResponse("hola mundo")

def bye(request): 
    return HttpResponse("chau mundo")

def edad(request, anios, futuro):

    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d  cumpliras %d años" %(futuro, cumplira) 

    return HttpResponse(mensaje)



