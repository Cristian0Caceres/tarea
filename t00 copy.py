import numpy as np 
class SistemaDeReservas:
    def __init__(self,filas,columnas):
        self.filas=filas
        self.columnas=columnas
        filas= self.filas
        columnas= self.columnas
        matriz = [[ __ for __ in range(columnas)] for __ in range(filas)]  
        for y in range(columnas):
            for x in range(filas):
                matriz[x][y] = 'N'
                vector = np.array(matriz)
                
        print(vector) 

    def reservar_asiento(self,fila,columna):
        
if __name__ == "__main__":
    cine = SistemaDeReservas(3, 7)
    print("Estado inicial del cine:")
    print(cine)
    resultado1 = cine.reservar_asiento(2, 3)
    print("Reserva exitosa:", resultado1)
    print("Estado del cine después de la reserva:")
    print(cine)
    resultado2 = cine.cancelar_reserva(2, 3)
    print("Cancelación exitosa:", resultado2)
    print("Estado del cine después de la cancelación:")
    print(cine)
    disponibles = cine.asientos_disponibles()
    print("Asientos disponibles:", disponibles)