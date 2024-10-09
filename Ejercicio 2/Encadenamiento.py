import numpy as np
from Hash import *

class Nodo: 
    __dato: object
    __sig: object
    
    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None
    
    def getDato(self):
        return self.__dato
    
    def setDato(self, dato):
        self.__dato = dato
    
    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig
        
class Encadenamiento:
    def __init__(self, dim):
        self.__dim = self.Primo(dim)
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
        pos = self.__hash.Division(clave, self.__dim)
        pos = self.__hash.Division(pos, self.__dim)
        aux = self.__tabla[pos]
        while (aux != None) and (aux.getSig() != None):
            aux = aux.getSig()
        if (aux == None):
            self.__tabla[pos] = Nodo(clave)
        else:
            aux.setSig(Nodo(clave))
    
    def Buscar(self, clave):
        comparaciones = 1
        pos = self.__hash.Division(clave, self.__dim)
        pos = self.__hash.Division(pos, self.__dim)
        aux = self.__tabla[pos]
        while (aux != None) and (aux.getDato() != clave):
            aux = aux.getSig()
            comparaciones += 1
        if (aux != None):
            if (aux.getDato() == clave):
                self.__comp_max_exito = max(self.__comp_max_exito, comparaciones)
                self.__comp_min_exito = min(self.__comp_min_exito, comparaciones)
            else:
                self.__comp_max_fracaso = max(self.__comp_max_fracaso, comparaciones)
                self.__comp_min_fracaso = min(self.__comp_min_fracaso, comparaciones)
        else:
            self.__comp_max_fracaso = max(self.__comp_max_fracaso, comparaciones)
            self.__comp_min_fracaso = min(self.__comp_min_fracaso, comparaciones)
    
    def Mostrar(self):
        for i in range(self.__dim):
            print (f"posicion {i}: ")
            aux = self.__tabla[i]
            while (aux != None):
                print(f"{aux.getDato()}")
                aux = aux.getSig()
    
    def Ej2(self):
        print(f"Comparaciones máximas en búsqueda exitosa: {self.__comp_max_exito}") 
        print(f"Comparaciones mínimas en búsqueda exitosa: {self.__comp_min_exito}")  
        print(f"Comparaciones máximas en búsqueda no exitosa: {self.__comp_max_fracaso}")  
        print(f"Comparaciones mínimas en búsqueda no exitosa: {self.__comp_min_fracaso}")