import numpy as np
from Hash import *

class Dir_Ab:
    def __init__(self, dim):
        self.__factor_carga = 0.7
        self.__dim = int(dim / self.__factor_carga)
        self.__dim = self.Primo(self.__dim)       
        self.__tabla = np.full(self.__dim, None, dtype = object)
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
        colisiones = 0
        pos = self.__hash.Alfanumerico(clave, self.__dim)
        if (self.__tabla[pos] == None):
            self.__tabla[pos] = clave
            self.__exito += 1
        else:
            nuevo = (pos + 1) % self.__dim
            colisiones += 1
            while (nuevo != pos) and (self.__tabla[nuevo] != None):
                nuevo = (nuevo + 1) % self.__dim
                colisiones += 1
            if (nuevo != pos):
                self.__tabla[nuevo] = clave
            else:
                print("No se pudo insertar la clave")
        self.__colisiones_totales += colisiones
        print(f"en la insersion, la clave {clave} colisionó {colisiones} veces")
    
    def Buscar(self, clave):
        pos = self.__hash.Alfanumerico(clave, self.__dim)
        if (self.__tabla[pos] == clave):
            print(f"clave {clave} encontrada en la psoición {pos}")
        else:
            nuevo = (pos + 1) % self.__dim
            while (nuevo != pos) and (self.__tabla[nuevo] != clave):
                nuevo = (nuevo + 1) % self.__dim
            if (nuevo != pos):
                print(f"clave {clave} encontrada en la psoición {nuevo}")
            else:
                print(f"clave {clave} no encontrada")
    
    def Mostrar(self):
        for i in range(self.__dim):
            print(f"posicion {i}: {self.__tabla[i]}")
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones_totales} colisiones")         