from django import views
from django.contrib import admin
from django.urls import path
from empleados import views

"""Estos son los paths de la applicacion que connectan a las funciones en el archivo views"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultar/', views.consultar),
    path('eliminar/', views.eliminar),
    path('actualizar/', views.actualizar),
]
