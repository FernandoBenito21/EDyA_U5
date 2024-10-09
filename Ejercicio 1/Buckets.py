import numpy as np
import math
from Hash import *

class Buckets:
    def __init__(self, m):
        self.__buckets = 4
        self.__filas = self.Primo(math.ceil((m / self.__buckets)))
        self.__sinonimas = np.full(int(self.__filas), 0, dtype = int)
        self.__filas = int(self.__filas * 1.2)
        self.__tabla = np.full((self.__filas, self.__buckets), None, dtype = object)
        self.__overflow = int(self.__filas / 1.2)
        self.__hash = Hash()
        self.__exito = 0
        self.__colisiones_totales = 0
    
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
        colisiones = 0
        if (self.__sinonimas[pos] < self.__buckets):
            self.__tabla[pos, self.__sinonimas[pos]] = clave
            colisiones = self.__sinonimas[pos]
            self.__sinonimas[pos] += 1
            print(f"Se insertó la clave {clave} tras {colisiones} colisiones")
            if (colisiones == 0):
                self.__exito += 1
        else:
            i = self.__overflow
            j = 0
            insertado = False
            while (i < self.__filas) and (insertado == False):
                while (j < self.__buckets) and (insertado == False):
                    colisiones += 1
                    if (self.__tabla[i, j] == None):
                        self.__tabla[i, j] = clave
                        self.__sinonimas[pos] += 1
                        insertado = True
                    else:
                        j += 1
                i += 1
                j = 0
            if (insertado == True):
                print(f"Se insertó la clave {clave}, en la zona de overflow tras {colisiones} colisiones")  
            else:
                print(f"La clave {clave} no se insertó")   
        self.__colisiones_totales += colisiones 
                  
                  
    def Buscar(self, clave):
        pos = self.__hash.Division(clave, (self.__filas * self.__buckets))
        pos = self.__hash.Division(pos, (self.__filas * self.__buckets))
        j = 0
        while (j < self.__buckets) and (self.__tabla[pos, j] != clave):
            j += 1
        if (j < self.__buckets):
            print(f"Se encontró la clave {clave} en la fila {pos}, columna {j}")
        else:
            if (self.__sinonimas[pos] > self.__buckets):
                i = self.__overflow
                j = 0
                encontrado = False
                while (i < self.__filas) and (encontrado == False):
                    while (j < self.__buckets) and (encontrado == False):
                        if (self.__tabla[i, j] == clave):
                            encontrado = True
                            j = self.__buckets
                            i = self.__filas
                        else:
                            j += 1
                    i += 1
                    j = 0
                if (encontrado == True):
                    print(f"Se encontró la clave {clave} en la zona de overflow, fila {i}, columna {j}")
                else:
                    print(f"La clave {clave} no se encontró")
            else:
                print(f"La clave {clave} no se encontró")
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones_totales} colisiones")
    
    def Mostrar(self):
        for i in range (self.__filas):
            if (i == self.__overflow):
                print("Zona de overflow: ")
            print(f"Fila {i}:")
            for j in range (self.__buckets):
                print(f"Columna {j}: {self.__tabla[i, j]}")