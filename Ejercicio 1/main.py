import random
from Direccionamiento_Abierto import *
from Encadenamiento import *
from Buckets import *


if __name__ == '__main__':
    tabla_D = Dir_Ab(5)
    tabla_E = Encadenamiento(5)
    tabla_B = Buckets(20)
    '''claves = []
    for i in range(20):
        clave = random.randint(100, 999)
        tabla_E.Insertar(clave)
        claves.append(clave)
    tabla_E.Datos()
    tabla_E.Mostrar()'''
    '''tabla_E.Insertar("E021")
    tabla_E.Insertar("A475")
    tabla_E.Insertar("a037")
    tabla_E.Insertar("b748")
    tabla_E.Insertar("Q789")
    tabla_E.Datos()
    tabla_E.Buscar("E021")
    tabla_B.Mostrar()'''
    tabla_B.Insertar(265)
    tabla_B.Insertar(325)
    tabla_B.Insertar(573)
    tabla_B.Insertar(261)
    tabla_B.Insertar(277)
    tabla_B.Insertar(198)
    tabla_B.Insertar(285)
    tabla_B.Buscar(265)
    tabla_B.Buscar(325)
    tabla_B.Buscar(573)
    tabla_B.Buscar(261)
    tabla_B.Buscar(198)
    tabla_B.Buscar(285)
    tabla_B.Datos()
    tabla_B.Mostrar()