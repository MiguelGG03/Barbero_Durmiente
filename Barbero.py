class Barbero:

    # Constructor
    def __init__(self):
        self.ocupado=False

    # Getters and Setters
    def isOcupado(self):
        return self.ocupado
    
    def setOcupado(self,ocupado:bool):
        self.ocupado=ocupado