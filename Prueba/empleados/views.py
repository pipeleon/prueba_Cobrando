from django.shortcuts import render

from empleados.models import Departamento, Empleado

"""Funciones que definen las vistas de la aplicacion"""

"""Funcion Consultar que se conecta con la base de datos para desplegar la lista de empleados
    tiene un Post request a la hora de añadir un nuevo empleado deacuerdo a la interacion con la applicacion
"""
def consultar(request):
    if request.method == "POST":
        departamento_query = Departamento.objects.filter(nombre=request.POST["departamento"])
        nuevo_empleado = Empleado(nif=request.POST["nif"],nombre=request.POST["nombre"], apellido1=request.POST["apellido1"], apellido2=request.POST["apellido2"], codigo_departamento=departamento_query[0])
        nuevo_empleado.save()

    """Coneccion con Base de Datos para busquedas"""
    empleados = Empleado.objects.all()
    departamentos = Departamento.objects.all()

    """Renderisa las vista deacuerdo a una platilla y las busquedas en forma de diccionario"""
    return render(request, "consultar.html", {"empleados":empleados, "departamentos": departamentos})

"""Funciona para actualizar un objeto deacuerdo a su ID y campo de busqueda"""
def actualizar(request):
    empleado = Empleado.objects.get(id=request.GET["id"])

    empleado.__setattr__(request.GET["atributo"], request.GET["nuevo"])
    empleado.save()

    return consultar(request)

"""Funcion para eliminar un objeto deacuerdo a su ID"""
def eliminar(request):
    Empleado.objects.get(id=request.GET["id"]).delete()

    return consultar(request)
