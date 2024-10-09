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
        pos = self.__hash.Division(clave, self.__dim)
        pos = self.__hash.Division(pos, self.__dim)
        aux = self.__tabla[pos]
        while (aux != None) and (aux.getSig() != None):
            aux = aux.getSig()
            colisiones += 1
        if (aux == None):
            self.__tabla[pos] = Nodo(clave)
        else:
            colisiones += 1
            aux.setSig(Nodo(clave))
        if (colisiones == 0):
            self.__exito += 1
        self.__colisiones_totales += colisiones
        print(f"Se insertó la clave {clave} tras {colisiones} colisiones")
    
    def Buscar(self, clave):
        pos = self.__hash.Division(clave, self.__dim)
        pos = self.__hash.Division(pos, self.__dim)
        aux = self.__tabla[pos]
        lugar = 0
        while (aux != None) and (aux.getDato() != clave):
            aux = aux.getSig()
            lugar += 1
        if (aux != None):
            if (aux.getDato() == clave):
                print(f"Se encontró la clave {clave} en la posición {pos}, lugar {lugar}")
            else:
                print(f"La clave {clave} no se encontró")
        else:
            print(f"La clave {clave} no se encontró")
    
    def Mostrar(self):
        for i in range(self.__dim):
            print (f"posicion {i}: ")
            aux = self.__tabla[i]
            while (aux != None):
                print(f"{aux.getDato()}")
                aux = aux.getSig()
    
    def Datos(self):
        print(f"se insertaron: {self.__exito} claves a la primera, hubo {self.__colisiones_totales} colisiones")