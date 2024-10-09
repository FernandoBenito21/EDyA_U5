import numpy as np
from Hash import *
import math

class Buckets:
    def __init__(self, m):
        self.__buckets = 4
        self.__filas = self.Primo(math.ceil((m / self.__buckets)))
        self.__sinonimas = np.full(int(self.__filas), 0, dtype = int)
        self.__filas = int(self.__filas * 1.2)
        self.__tabla = np.full((self.__filas, self.__buckets), None, dtype = object)
        self.__overflow = int(self.__filas / 1.2)
        self.__hash = Hash()
        self.__comp_min_exito = 9999
        self.__comp_max_exito = 0   
        self.__comp_min_fracaso = 9999
        self.__comp_max_fracaso = 0 
    
    def Primo(self, x):
        i = 2
        while (i < x) and ((x % i) != 0):
            i += 1
        if (i == x):
            return x
        else:
            return self.Primo(x + 1)
    
    def Insertar(self, clave):
        pos = self.__hash.Division(clave, (self.__filas * self.__buckets))
        pos = self.__hash.Division(pos, (self.__filas * self.__buckets))
        if (self.__sinonimas[pos] < self.__buckets):
            self.__tabla[pos, self.__sinonimas[pos]] = clave
            self.__sinonimas[pos] += 1
        else:
            i = self.__overflow
            j = 0
            insertado = False
            while (i < self.__filas) and (insertado == False):
                while (j < self.__buckets) and (insertado == False):
                    if (self.__tabla[i, j] == None):
                        self.__tabla[i, j] = clave
                        self.__sinonimas[pos] += 1
                        insertado = True
                    else:
                        j += 1
                i += 1
                j = 0
                    

    def Buscar(self, clave):
        comparaciones = 1
        pos = self.__hash.Division(clave, (self.__filas * self.__buckets))
        pos = self.__hash.Division(pos, (self.__filas * self.__buckets))
        j = 0
        while (j < self.__buckets) and (self.__tabla[pos, j] != clave):
            comparaciones += 1
            j += 1
        if (j < self.__buckets):
            self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
            self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
        else:
            if (self.__sinonimas[pos] > self.__buckets):
                i = self.__overflow
                j = 0
                encontrado = False
                while (i < self.__filas) and (encontrado == False):
                    while (j < self.__buckets) and (encontrado == False):
                        comparaciones += 1
                        if (self.__tabla[i, j] == clave):
                            self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
                            self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
                            encontrado = True
                        else:
                            j += 1
                    i += 1
                    j = 0
                if (encontrado == True):
                    self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
                    self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
                else:
                    self.__comp_max_fracaso = max(self.__comp_max_fracaso, comparaciones)
                    self.__comp_min_fracaso = min(self.__comp_min_fracaso, comparaciones)
            else:
                self.__comp_max_fracaso = max(self.__comp_max_fracaso, comparaciones)
                self.__comp_min_fracaso = min(self.__comp_min_fracaso, comparaciones)
    
    def Mostrar(self):
        for i in range (self.__filas):
            if (i == self.__overflow):
                print("Zona de overflow: ")
            print(f"Fila {i}:")
            for j in range (self.__buckets):
                print(f"Columna {j}: {self.__tabla[i, j]}")
    
    def Ej2(self):
        print(f"Comparaciones máximas en búsqueda exitosa: {self.__comp_max_exito}") 
        print(f"Comparaciones mínimas en búsqueda exitosa: {self.__comp_min_exito}")  
        print(f"Comparaciones máximas en búsqueda no exitosa: {self.__comp_max_fracaso}")  
        print(f"Comparaciones mínimas en búsqueda no exitosa: {self.__comp_min_fracaso}")