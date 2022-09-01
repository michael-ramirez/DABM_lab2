# -*- coding: utf-8 -*-

import datetime
from tabulate import tabulate

class Equipos:
    def __init__(self, nombre, proveedor, cantidad, referencia, ciclo, fum = "", disponibles = ""):
        self.nombre = nombre
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum
        self.disponibles = disponibles

    
    def verDatos(self):
        header = ["NOMBRE", "PROVEEDOR", "CANTIDAD","REFERENCIA", "CICLO", "FUM", "DISPONIBLES"]
        datos = [[self.nombre, self.proveedor, self.cantidad, self.referencia, self.ciclo, self.fum, self.disponibles]]
        print(tabulate((datos, header), tablefmt = "grid"))

    def save(self):
        file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\Equipos.csv', 'a')
        linea = ";".join([self.nombre, self.proveedor, self.cantidad, self.referencia, self.ciclo, self.fum, self.disponibles])
        file.write(linea+"\n")
        file.close()
        


def crearEquipo():
    print("REGISTRAR NUEVO EQUIPO")
    nombre = input("Nombre: ")

    if len(nombre) == 0:
        print("Nombre inválido")
        crearEquipo()
    proveedor = input("Proveedor: ")
    referencia = input("Referencia: ")
    ciclo = input("Ciclo de mantenimiento (dìas): ")
    cantidad = input("Cantidad: ")
    fecha = input("Ingrese la fecha de último mantenimiento (yyyy-mm-dd): ")
    disponibles = cantidad
    e = Equipos(nombre, proveedor, referencia, ciclo, cantidad, fecha, disponibles)
    
    return e

def consultarEquipo():
    equipo = input("Ingrese el nombre del equipo: ")
    header = ["NOMBRE", "PROVEEDOR", "REFERENCIA", "CICLO", "CANTIDAD", "FUM", "DISPONIBLES"]
    datos = getAllEquipos()
      
    for articulo in datos:
        if articulo[0] == equipo:
            print(tabulate([articulo],header,tablefmt="grid"))


def registroMantenimiento():
    equipo = input("Ingrese el nombre del equipo: ")    
    fecha = input("Ingrese la fecha de último mantenimiento: ")
    header = ["NOMBRE", "PROVEEDOR", "CANTIDAD","REFERENCIA", "CICLO", "FUM", "DISPONIBLES"]
                      
    datos = getAllEquipos()
    
    for i in range(len(datos)):
        articulo = datos[i]
        if articulo[0] == equipo:
            articulo[len(articulo)-2] = fecha
            datos[i] = articulo
            print(tabulate(datos,header,tablefmt="grid"))

    saveAllEquipos(datos)

def consultaMantenimiento():
    fechaInicio = input("Ingrese fecha de inicio (yyyy-mm-dd): ")
    fechaFin = input("Ingrese fecha de final (yyyy-mm-dd): ")
    date1 = datetime.datetime.strptime(fechaInicio, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(fechaFin, "%Y-%m-%d")
    dif = (date2 - date1).days
    
    datos = getAllEquipos()
    pos = 0
    for articulo in datos:
        fum = datetime.datetime.strptime(articulo[5][:10], "%Y-%m-%d")
        fum = fum + datetime.timedelta(days=int(articulo[4]))
        fecha = date1
        for i in range(0,dif):
             fecha = fecha + datetime.timedelta(days=1)
             if fum == fecha:
                 print("Se debe realizar mantenimiento al equipo {} en la fecha {}".format(articulo[0],fecha.strftime("%Y-%m-%d")))
                 pos =+ 1
                 break
    
    if pos == 0:
        print("No se debe realizar mantenimientos en este rango de fechas")        


def getAllEquipos():
    file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\Equipos.csv', 'r')
    lineas = file.readlines()
    datos = []

    for l in lineas:
      l = l.replace("⧵n","")
      l = l.split(";")
      datos.append(l)
    
    return datos

def saveAllEquipos(datos):
    file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\Equipos.csv', 'w')
    for i in range(len(datos)):        
        linea = ";".join(datos[i])
        file.write(linea)

    file.close()
    
    