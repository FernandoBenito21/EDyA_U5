import numpy as np
from Hash import *

class Buckets:
    def __init__(self, m):
        self.__factor_carga = 0.7
        self.__columnas = 4
        self.__filas = self.Primo(m // (self.__columnas * self.__factor_carga))
        self.__overflow = int(self.__filas)
        self.__sinonimas = np.full(int(self.__filas), 0, dtype = int)
        self.__filas = int(self.__filas * 1.2)
        self.__tabla = np.full((self.__filas, self.__columnas), None, dtype = object)
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
        pos = self.__hash.Division(clave, self.__filas)
        pos = self.__hash.Division(pos, self.__filas)
        pasadas = 0
        j = 0
        while (j < self.__columnas) and (self.__tabla[pos, j] != None):
            j += 1
            self.__colisiones += 1
            pasadas += 1
        if (j < self.__columnas):
            self.__tabla[pos, j] = clave
            self.__sinonimas[pos] += 1
            if (pasadas == 0):
                self.__exito += 1
            print (f"Clave {clave} insertada tras {pasadas} colisiones")
        else:
            i = self.__overflow
            k = 0
            while (i < self.__filas) and (self.__tabla[i, k] != None):
                if (k < self.__columnas):
                    k += 1
                    pasadas +=1
                    self.__colisiones = 0
                else:
                    k = 0
                    i += 1
            if (i < self.__filas):
                self.__tabla[i, k] = clave
                self.__sinonimas[pos] += 1
                print (f"La clave {clave} se insertó en el área de overflow tras {pasadas} colisiones")
            else:
                print(f"La clave {clave} no se pudo insertar")
    
    def Buscar(self, clave):
        pos = self.__hash.Division(clave, self.__filas)
        pos = self.__hash.Division(pos, self.__filas)
        j = 0
        while (j < self.__columnas) and (self.__tabla[pos, j] != clave):
            j += 1
        if (j < self.__columnas):
            print(f"Clave {clave} encontrada en la fila {pos}, columna {j}")
        else:
            if (self.__sinonimas[pos] > self.__columnas):
                i = self.__overflow
                k = 0
                while (i < self.__filas) and (self.__tabla[i, k] != clave):
                    if (k < self.__columnas):
                        k += 1
                    else:
                        k = 0
                        i += 1
                if (i < self.__filas):
                    print(f"La clave {clave} se encontró en el área de overflow, fila {i}, columna {k}")
                else:
                    print("La clave no se encontró")
            else:
                print("La clave no se encontró")
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones} colisiones")
    
    def Mostrar(self):
        for i in range (self.__filas):
            if (i == self.__overflow):
                print("Zona de overflow: ")
            print(f"Fila {i}:")
            for j in range (self.__columnas):
                print(f"Columna {j}: {self.__tabla[i, j]}")