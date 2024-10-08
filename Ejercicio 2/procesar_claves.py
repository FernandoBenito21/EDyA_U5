import csv

class ManejaArchivo:
    def __init__(self):
        self.__claves = []

    def Archivo(self):
        try:
            with open('claves_aleatorias.csv', 'r') as archivo:
                for linea in archivo:
                    clave = linea.strip()
                    if clave:
                        self.__claves.append(clave)
        except FileNotFoundError:
            print(f"Error: El archivo claves_aleatorias.csv no se encontró.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

    def getClaves(self):
        return self.__claves
