import numpy as np
import random as rd 
class Matriz:
    def __init__(self, filas, columnas, aleatoria=False):
        self.filas = filas                                 # Un entero que indica el número de filas en la matriz
        self.columnas = columnas                           # Un entero que indica el número de columnas en la matriz.
        self.aleatorio = aleatoria                         # Un valor booleano que, si es verdadero, inicializa la matriz con valores aleatorios entre 0 y 9
        self.elementos = []                                # Una lista de listas que contiene los elementos de la matriz.
    
    def imprimir(self) :
        matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)] 
        i = 0  
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.aleatorio == False:
                    matriz[x][y] = 0
                    self.elementos.append(matriz[x][y])
                else:
                    matriz[x][y] = rd.randrange(10)
                    self.elementos.append(matriz[x][y])
                i += 1         
        vector = np.array(matriz)
        print(vector)  

    def sumar(self, otra):
        matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)] 
        matriz2 = [[ __ for __ in range(otra.columnas)] for __ in range(otra.filas)] 
        i = 0  
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.aleatorio == False and otra.aleatorio == False:
                    matriz[x][y] = 0
                    matriz2[x][y] = 0

                elif self.aleatorio == False and otra.aleatorio == True:
                    matriz[x][y] = 0
                    matriz2[x][y] = otra.elementos[i]

                elif self.aleatorio == True and otra.aleatorio == False:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = 0
                elif self.aleatorio == True and otra.aleatorio == True:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = otra.elementos[i]
                i += 1
        for x in range(self.filas):
            for y in range(self.columnas):
                matriz[x][y] += matriz2[x][y]
        vector = np.array(matriz)
        print(vector) 

    def restar(self, otra):
        matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)] 
        matriz2 = [[ __ for __ in range(otra.columnas)] for __ in range(otra.filas)] 
        i = 0  
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.aleatorio == False and otra.aleatorio == False:
                    matriz[x][y] = 0
                    matriz2[x][y] = 0

                elif self.aleatorio == False and otra.aleatorio == True:
                    matriz[x][y] = 0
                    matriz2[x][y] = otra.elementos[i]

                elif self.aleatorio == True and otra.aleatorio == False:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = 0
                elif self.aleatorio == True and otra.aleatorio == True:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = otra.elementos[i]
                i += 1
        for x in range(self.filas):
            for y in range(self.columnas):
                matriz[x][y] -= matriz2[x][y]
    def multiplicar(self, otra):
        matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)] 
        matriz2 = [[ __ for __ in range(otra.columnas)] for __ in range(otra.filas)] 
        i = 0  
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.aleatorio == False and otra.aleatorio == False:
                    matriz[x][y] = 0
                    matriz2[x][y] = 0

                elif self.aleatorio == False and otra.aleatorio == True:
                    matriz[x][y] = 0
                    matriz2[x][y] = otra.elementos[i]

                elif self.aleatorio == True and otra.aleatorio == False:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = 0
                elif self.aleatorio == True and otra.aleatorio == True:
                    matriz[x][y] = self.elementos[i]
                    matriz2[x][y] = otra.elementos[i]
                i += 1
        for x in range(self.filas):
            for y in range(self.columnas):
                matriz[x][y] *= matriz2[x][y]

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
