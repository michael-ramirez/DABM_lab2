# -*- coding: utf-8 -*-
from tabulate import tabulate
from Clases.equipo import *

class Prestamo:
    file = "C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\prestamos.csv"
    def __init__(self, nombre, carnet, equipo, fechap, fechae):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fechap = fechap
        self.fechae = fechae
        
    def save(self):
        f = open(self.file,"a")
        linea = ";".join([self.nombre,self.carnet,self.equipo,self.fechap,self.fechae])
        f.write(linea+"\n")
        f.close()
        


def crearPrestamo():
    print("REGISTRAR PRESTAMO")
    datos = getAllEquipos()
    
    nombre = input("Nombre del estudiante: ")
    carnet = input("Carnet: ")
    equipo = input("Equipo: ")
    
    pos = 1
    for articulo in datos:
        if articulo[0] == equipo:
            break
        elif articulo[0] == equipo and pos == len(datos) :
            print("No se encuentra el equipo")
            crearPrestamo()
        pos =+ 1

    fechap = input("Fecha de prestamo (yyyy-mm-dd): ")
    fechae = input("Fecha de entrega (yyyy-mm-dd): ")
    p = Prestamo(nombre, carnet, equipo, fechap, fechae)
    return p

def verPrestamos():
    carnet = input("Ingrese el número de carnet: ")
    file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\prestamos.csv', 'r')
    lineas = file.readlines()
    header = ["NOMBRE", "CARNET", "EQUIPO", "FECHA DE PRESTAMO", "FECHA DE ENTREGA"]
    datos = []

    for l in lineas:
      l = l.replace("⧵n","")
      l = l.split(";")
      datos.append(l)
      
    for articulo in datos:
        if articulo[1] == carnet:
            print(tabulate([articulo],header,tablefmt="grid"))
                
    file.close()

def actualizarEquipos():
    datos = getAllEquipos()
    prestamos = getAllPrestamos()

    for i in range(len(datos)):
        articulo = datos[i]
        if articulo[0] == prestamos[len(prestamos)-1][2]:
            articulo[len(articulo)-1] = str(int(articulo[len(articulo)-1]) - 1)
            datos[i] = articulo

    saveAllEquipos(datos)
    closePrestamos()
    
def getAllPrestamos():
    file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\prestamos.csv', 'r')
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
        
def closePrestamos():
    file = open('C:\Programación\Python\Diseño Aplicaciones\Laboratorio_2\Databases\prestamos.csv', 'r')
    file.close()
