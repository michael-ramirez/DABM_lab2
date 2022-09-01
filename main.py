# -*- coding: utf-8 -*-
"""
@author: Michael Ramirez

Diseño de aplicaciones biomédicas

Laboratorio 2
"""

from Clases.menu import *
from Clases.equipo import *
from Clases.prestamo import *

def main():
    menu = Menu("Escuela de Ingenierìa")
    op = menu.ver()
    if op == "1":
        menu2 = MenuTecnicos()
        op2 = menu2.ver()
        if op2 == "1":
            e = crearEquipo()
            e.save()
        elif op2 == "2":
            p = crearPrestamo()
            p.save()
            actualizarEquipos()
        elif op2 == "3":
            consultaMantenimiento()
        elif op2 == "4":
            registroMantenimiento()
        else: 
            print("Opción inválida")
            main()
    
    elif op == "2":
        menu2 = MenuEstudiantes()
        op2 = menu2.ver()
        if op2 == "1":
            verPrestamos()
        elif op2 == "2":
            consultarEquipo() 
            
    elif op == "3":
        return
        
    main()

if __name__ == '__main__':    
    main()
