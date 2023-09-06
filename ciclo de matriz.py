import numpy as np 
filas = 3
columnas = 4

elemento = [1,1,1,2,2,2,3,3,3,4,4,4,4]

matriz = [[ __ for __ in range(filas)] for __ in range(columnas)]   
lista_e = len(elemento)


for x in range(columnas):
    for y in range(filas):
        matriz[x][y] = 'N'
vector = np.array(matriz)
print(vector)