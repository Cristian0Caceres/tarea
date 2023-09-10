import numpy as np 
class SistemaDeReservas:
    def __init__(self,filas,columnas):
        self.filas=filas
        self.columnas=columnas
        self.matriz = [[ __ for __ in range(self.columnas)] for __ in range(self.filas)]  
        for y in range(self.columnas):
            for x in range(self.filas):
                 self.matriz[x][y] = 'Dis'
    def MuestraEstadoCine(self):         
        vector = np.array(cine.matriz)
        print(vector)        
    

    def reservar_asiento(self,fila,columna):
        posx=fila
        posy=columna
        cine.matriz[posx][posy] = "res"
        return "True"
    def cancelar_reserva(self,fila,columna):
        posx=fila
        posy=columna
        cine.matriz[posx][posy] = "Dis"
        return "True"
    def asientos_disponibles(self):
        disp=0
        for x in range(0, self.filas -1):
            for y in range(0,self.columnas -1):
                if cine.matriz[x][y]=="dis":
                    dis += 1

        return disp
if __name__ == "__main__":
    cine = SistemaDeReservas(3, 7)
    print("Estado inicial del cine:")
    print(cine.MuestraEstadoCine())
    resultado1 = cine.reservar_asiento(2, 3)
    print("Reserva exitosa:", resultado1)
    print("Estado del cine después de la reserva:")
    print(cine.MuestraEstadoCine())
    resultado2 = cine.cancelar_reserva(2, 3)
    print("Cancelación exitosa:", resultado2)
    print("Estado del cine después de la cancelación:")
    print(cine.MuestraEstadoCine())
    disponibles = cine.asientos_disponibles()
    print("Asientos disponibles:", disponibles)