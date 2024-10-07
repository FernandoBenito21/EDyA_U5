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
        self.__factor_carga = 1
        self.__dim = self.Primo(int(dim * self.__factor_carga))
        self.__tabla = np.full(self.__dim, None, dtype = object)
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
        pasadas = 0
        nodo = Nodo(clave)
        pos = self.__hash.Alfanumerico(clave, self.__dim)
        aux = self.__tabla[pos]
        while (aux.getSig() != None):
            aux = aux.getSig()
            pasadas += 1
            self.__colisiones += 1
        aux.setSig(nodo)
        if (pasadas == 0):
            self.__exito += 1
        print(f"La clave {clave} colisionó {pasadas} veces")
    
    def Buscar(self, clave):
        lugar = 0
        pos = self.__hash.Alfanumerico(clave, self.__dim)
        aux = self.__tabla[pos].getSig()
        while (aux != None) and (aux.getDato() != clave):
            aux = aux.getSig()
            lugar += 1
        if (aux != None):
            print(f"Clave {clave} encontrada en la posición {pos}, tras {lugar} colisiones")
        else:
            print(f"Clave no encontrada")
    
    def Mostrar(self):
        for i in range(self.__dim):
            print (f"posicion {i}: ")
            aux = self.__tabla[i]
            while (aux != None):
                print(f"{aux.getDato()}")
                aux = aux.getSig()
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones} colisiones")