#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def hello(request): 
    return HttpResponse("hola mundo")

def bye(request): 
    return HttpResponse("chau mundo")

def edad(request, anios, futuro):

    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d  cumpliras %d años" %(futuro, cumplira) 

    return HttpResponse(mensaje)

def primer_plantilla(request):
    plantilla = """
    <htnl>
      <body>
        <h2> 
          Hola {{nombre}} estas es mi primer plantilla 
        </h2>
      </body>
    </html>
"""

    tpl = Template(plantilla)
    ctx = Context({
        "nombre": "Julio Martinez"
    })
    mensaje = tpl.render(ctx)

    return HttpResponse(mensaje)

def segunda_plantilla(request):
    

    tpl = get_template("segunda_plantilla.html")

    mensaje = tpl.render({
        
        "nombre": "Julio Martinez",
        "fecha_actual": date.today()
    })
    return HttpResponse(mensaje)

def tercer_plantilla(request):
    
   return render(request,"tercer_plantilla.html",{
      "nombre": "Julio Martinez",
        "fecha_actual": date.today()
      
   })

class Empleado(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

def cuarta_plantilla(request):
   
   empleado = Empleado("Julio","Martinez")

   laborables = ["lunes","martes","miercoles", "jueves"]
    
   return render(request,"cuarta_plantilla.html",{
      "mi_empleado": empleado,
        "fecha_actual": date.today(),
        "dias_laborables": laborables
      
   })






