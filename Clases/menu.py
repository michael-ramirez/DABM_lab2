# -*- coding: utf-8 -*-

class Menu:
  def __init__(self, laboratorio):
    self.laboratorio = laboratorio

  def ver(self):
    print("BIENVENIDO AL SISTEMA".center(50,"*"))
    print("Laboratorio : "+self.laboratorio)
    print("1. Tecnicos")
    print("2. Estudiantes")
    print("3. Salir")
    op = input(">>>")

    return op

class MenuTecnicos:

    def ver(self):
        print("MENU TÈCNICOS DE LABORATORIO".center(20,"*"))
        print("1. Registrar equipos")
        print("2. Registrar prestamo")
        print("3. Consultar equipos para hacer mantenimiento en un rango de fechas")
        print("4. Registar mantenimiento")
        op = input(">>>")
        
        return op

class MenuEstudiantes:

    def ver(self):
        print("MENU ESTUDIANTES".center(20,"*"))
        print("1. Ver equipos en prestamo")
        print("2. Ver disponibilidad de equipos")
        op = input(">>>")
        
        return op

