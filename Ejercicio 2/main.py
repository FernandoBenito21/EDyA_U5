from Direccionamiento_Abierto import *
from Encadenamiento import *
from Buckets import *
from procesar_claves import *
import random

if __name__ == '__main__':
    Tabla_D = Dir_Ab(100)
    Tabla_E = Encadenamiento(100)
    Tabla_B = Buckets(100)
    archivo = ManejaArchivo()
    archivo.Archivo()
    claves = archivo.getClaves()
    for i in range(len(claves)):
        clave = claves[i]
        Tabla_D.Insertar(clave)
        Tabla_E.Insertar(clave)
        Tabla_B.Insertar(clave)
    for i in range(len(claves)):
        clave = claves[i]
        Tabla_D.Buscar(clave)
        Tabla_E.Buscar(clave)
        Tabla_B.Buscar(clave)
    for i in range(len(claves)):
        num = random.randint(100, 200)
        Tabla_D.Buscar(num)
        Tabla_E.Buscar(num)
        Tabla_B.Buscar(num)
    print("Resultados finales: ")
    print("Para Direccionamiento Abierto: ")
    Tabla_D.Ej2()
    print("Para Encadenamiento: ")
    Tabla_E.Ej2()
    print("Para Buckets: ")
    Tabla_B.Ej2()