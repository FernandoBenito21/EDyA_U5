import numpy as np
from Hash import *

class Dir_Ab:
    def __init__(self, dim):
        self.__factor_carga = 0.7
        self.__dim = int(dim / self.__factor_carga)
        self.__dim = self.Primo(self.__dim)       
        self.__tabla = np.full(self.__dim, None, dtype = object)
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
        pos = self.__hash.Plegado(clave, 3, self.__dim)
        pos = self.__hash.Extraccion(pos, 1)
        pos = self.__hash.Division(pos, self.__dim)
        if (self.__tabla[pos] == None):
            self.__tabla[pos] = clave
        else:
            nuevo = (pos + 1) % self.__dim
            while (nuevo != pos) and (self.__tabla[nuevo] != None):
                nuevo = (nuevo + 1) % self.__dim
            if (nuevo != pos):
                self.__tabla[nuevo] = clave
    
    def Buscar(self, clave):
        comparaciones = 1
        pos = self.__hash.Plegado(clave, 3, self.__dim)
        pos = self.__hash.Extraccion(pos, 1)
        pos = self.__hash.Division(pos, self.__dim)
        if (self.__tabla[pos] == clave):
            self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
            self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
        else:
            nuevo = (pos + 1) % self.__dim
            comparaciones += 1
            while (nuevo != pos) and (self.__tabla[nuevo] != clave):
                nuevo = (nuevo + 1) % self.__dim
                comparaciones += 1
            if (nuevo != pos):
                self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
                self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
            else:
                self.__comp_max_fracaso = max(self.__comp_max_fracaso, comparaciones)
                self.__comp_min_fracaso = min(self.__comp_min_fracaso, comparaciones)
    
    def Mostrar(self):
        for i in range(self.__dim):
            print(f"posicion {i}: {self.__tabla[i]}")
    
    def Ej2(self):
        print(f"Comparaciones máximas en búsqueda exitosa: {self.__comp_max_exito}") 
        print(f"Comparaciones mínimas en búsqueda exitosa: {self.__comp_min_exito}")  
        print(f"Comparaciones máximas en búsqueda no exitosa: {self.__comp_max_fracaso}")  
        print(f"Comparaciones mínimas en búsqueda no exitosa: {self.__comp_min_fracaso}")            