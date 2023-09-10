
import random as rd 
class Matriz:
    def __init__(self, filas, columnas, aleatoria=False):
        self.filas = filas                                 # Un entero que indica el número de filas en la matriz
        self.columnas = columnas                           # Un entero que indica el número de columnas en la matriz.
        self.aleatorio = aleatoria                         # Un valor booleano que, si es verdadero, inicializa la matriz con valores aleatorios entre 0 y 9
        self.elementos = []                                # Una lista de listas que contiene los elementos de la matriz.
        matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)] 
        i = 0  
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.aleatorio == False:
                    matriz[x][y] = 0
                    self.elementos += [matriz[x][y]] 
                else:
                    matriz[x][y] = rd.randrange(10)
                    self.elementos += [matriz[x][y]]
                i += 1         
    def imprimir(self) :
        inicio = 0
        final =  len(self.elementos)//self.columnas
        for num in range(self.filas):            #recorrer por cantidad de filas
            print(self.elementos[inicio:final])
            inicio = final
            final += len(self.elementos)//self.columnas
    def sumar(self,otra):
        Matriz_s = Matriz(self.filas,self.columnas)
        i = 0
        if self.aleatorio ==  Matriz.__str__(otra.aleatorio) == False:
            return Matriz_s

        elif self.aleatorio == True and Matriz.__str__(otra.aleatorio) == True:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_s.elementos[i] = self.elementos[i] +  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        else:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_s.elementos[i] = self.elementos[i] +  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        return Matriz_s
    
    def restar(self, otra):
        Matriz_r = Matriz(self.filas,self.columnas)
        i = 0
        if self.aleatorio ==  Matriz.__str__(otra.aleatorio) == False:
            return Matriz_r

        elif self.aleatorio == True and Matriz.__str__(otra.aleatorio) == True:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_r.elementos[i] = self.elementos[i] -  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        else:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_r.elementos[i] = self.elementos[i] -  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        return Matriz_r
            
    def multiplicar(self, otra):
        Matriz_m = Matriz(self.filas,self.columnas)
        i = 0
        if self.aleatorio ==  Matriz.__str__(otra.aleatorio) == False:
            return Matriz_m

        elif self.aleatorio == True and Matriz.__str__(otra.aleatorio) == True:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_m.elementos[i] = self.elementos[i] *  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        else:
            for x in range(self.filas):
                for y in range(self.columnas):
                    Matriz_m.elementos[i] = self.elementos[i] *  int(Matriz.__str__(otra.elementos[i]))
                    i += 1
        return Matriz_m
    
import random
if __name__ == "__main__":
    random.seed(7)
    matriz1 = Matriz(5, 5, True)
    random.seed(8)
    matriz2 = Matriz(5, 5, True)
    print("Matriz 1:")
    matriz1.imprimir()
    print("Matriz 2:")
    matriz2.imprimir()
    suma = matriz1.sumar(matriz2)
    print("Resultado de la suma:")
    suma.imprimir()
    resta = matriz1.restar(matriz2)
    print("Resultado de la resta:")
    resta.imprimir()
    multiplicacion = matriz1.multiplicar(matriz2)
    print("Resultado de la multiplicación:")
    multiplicacion.imprimir()    