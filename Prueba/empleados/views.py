from django.shortcuts import render

from empleados.models import Departamento, Empleado

# Create your views here.

def consultar(request):
    if request.method == "POST":
        departamento_query = Departamento.objects.filter(nombre=request.POST["departamento"])
        nuevo_empleado = Empleado(nif=request.POST["nif"],nombre=request.POST["nombre"], apellido1=request.POST["apellido1"], apellido2=request.POST["apellido2"], codigo_departamento=departamento_query[0])
        nuevo_empleado.save()

    empleados = Empleado.objects.all()
    departamentos = Departamento.objects.all()

    return render(request, "consultar.html", {"empleados":empleados, "departamentos": departamentos})

def eliminar(request):
    Empleado.objects.get(id=request.GET["id"]).delete()

    return consultar(request)
