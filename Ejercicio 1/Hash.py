class Hash:
                  
    def Division(self, clave, dim):
        retorna = clave % dim
        return retorna
    
    def Extraccion(self, clave, n):
        clave_str = str(clave)
        retorna = clave_str[-n:]
        retorna = int(retorna)
        return retorna
    
    def Plegado(self, clave, longitud_bloque, dim):
        clave_str = str(clave)
        suma = 0
        for i in range(0, len(clave_str), longitud_bloque):
            bloque = clave_str[i : (i+longitud_bloque)]
            suma += int(bloque)
        retorna = suma % dim
        return retorna
   
    def Cuadrado_Medio(self, clave, dim):
        cuadrado = clave ** 2
        cuadrado_str = str(cuadrado)
        medio = len(cuadrado_str) // 2
        if len(cuadrado_str) % 2 == 0:
            extraido = cuadrado_str[medio-1 : medio+1]
        else:
            extraido = cuadrado_str[medio]
        retorna = int(extraido) % dim
        return retorna
    
    def Alfanumerico(self, clave, dim):
        clave_str = str(clave)
        suma = sum([ord(caracter) for caracter in clave_str])
        retorna = suma % dim
        return retorna
