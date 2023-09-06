import numpy as np 
filas = 3
columnas = 4

elemento = [1,1,1,2,2,2,3,3,3,4,4,4]

matriz = [[ __ for __ in range(columnas)] for __ in range(filas)] 
i = 0  
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = elemento[i]
        i += 1
vector = np.array(matriz)
print(vector)