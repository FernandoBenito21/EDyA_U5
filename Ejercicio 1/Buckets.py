import numpy as np
import math
from Hash import *

class Buckets:
    def __init__(self, m):
        self.__buckets = 4
        self.__filas = self.Primo(math.ceil((m / self.__buckets)))
        self.__filas = int(self.__filas * 1.2)
        self.__sinonimas = np.full(int(self.__filas), 0, dtype = int)
        self.__tabla = np.full((self.__filas, self.__buckets), None, dtype = object)
        self.__overflow = int(self.__filas / 1.2)
        self.__hash = Hash()
        self.__exito = 0
        self.__colisiones = 0
    
    def Primo(self, x):
        i = 2
        while (i < x) and ((x % i) != 0):
            i += 1
        if (i == x):
            return x
        else:
            return self.Primo(x + 1)
    
    def Insertar(self, clave):
        pos = self.__hash.Plegado(clave, 2, self.__filas)
        pos = self.__hash.Extraccion(pos, 1)
        pasadas = 0
        if (self.__sinonimas[pos] < self.__buckets):
            self.__tabla[pos, self.__sinonimas[pos]] = clave
            self.__colisiones += self.__sinonimas[pos]
            pasadas = self.__sinonimas[pos]
            self.__sinonimas[pos] += 1
            print(f"Se insertó la clave {clave} tras {pasadas} colisiones")
            if (pasadas == 0):
                self.__exito += 1
        else:
            i = self.__overflow
            j = 0
            exito = False
            while (i < self.__filas):
                while (j < self.__buckets):
                    self.__colisiones += 1
                    pasadas += 1
                    if (self.__tabla[i, j] == None):
                        self.__tabla[i, j] = clave
                        self.__sinonimas[pos] += 1
                        exito = True
                        j = self.__buckets
                        i = self.__filas
                    else:
                        j += 1
                i += 1
                j = 0
            if (exito == True):
                print(f"Se insertó la clave {clave}, en la zona de overflow tras {pasadas} colisiones")  
            else:
                print(f"La clave {clave} no se insertó")    
                  
                  
    def Buscar(self, clave):
        pos = self.__hash.Plegado(clave, 2, self.__filas)
        pos = self.__hash.Extraccion(pos, 1)
        j = 0
        while (j < self.__buckets) and (self.__tabla[pos, j] != clave):
            j += 1
        if (j < self.__buckets):
            print(f"Se encontró la clave {clave} en la fila {pos}, columna {j}")
        else:
            if (self.__sinonimas[pos] > self.__buckets):
                i = self.__overflow
                j = 0
                exito = False
                while (i < self.__filas):
                    while (j < self.__buckets):
                        if (self.__tabla[i, j] == clave):
                            exito = True
                            j = self.__buckets
                            i = self.__filas
                        else:
                            j += 1
                    i += 1
                    j = 0
                if (exito == True):
                    print(f"Se encontró la clave {clave} en la zona de overflow, fila {i}, columna {j}")
                else:
                    print(f"La clave {clave} no se encontró")
            else:
                print(f"La clave {clave} no se encontró")
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones} colisiones")
    
    def Mostrar(self):
        for i in range (self.__filas):
            if (i == self.__overflow):
                print("Zona de overflow: ")
            print(f"Fila {i}:")
            for j in range (self.__buckets):
                print(f"Columna {j}: {self.__tabla[i, j]}")
