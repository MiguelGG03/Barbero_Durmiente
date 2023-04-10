import random

class Cliente:

    # Constructor de la clase
    def __init__(self,numCliente,estado):
        self.numCliente=numCliente
        self.estado=estado
        self.tiempoEsperado=0
        self.tiempoDeEspera=random.randrange(5,25)

    # Getters and Setters
    def getNumCliente(self):
        return self.numCliente
    
    def setNumCliente(self,x:int):
        self.numCliente=x

    def getEstado(self):
        return self.estado
    
    def setEstado(self,x:str):
        self.estado=x
        