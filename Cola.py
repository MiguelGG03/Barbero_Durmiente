# Este script se va a utilizar para la creacion de un programa que
# atienda a los clientes de la barberia

from Cliente import Cliente

class Cola:
    """Clase que representa una cola de clientes
    con metodos/funciones para encolar o desencolar
    clientes
    """
    def __init__(self):
        """ Creacion de una cola vacia """
        self.items = []

    def estaVacia(self):
        """ Metodo que verifica si la cola esta vacia """
        return self.items == []
    
    def encolar(self, item):
        """ Metodo que agrega un cliente a la cola como último elemento """
        self.items.append(item)

    def first(self):
        """ Metodo que devuelve el primer elemento de la cola """
        try:
            return self.items[0]
        except IndexError:
            print("La cola esta vacia")
            return self.items

    def desencolar(self):
        """ Metodo que elimina el primer elemento de la cola """
        return self.items.pop(0)
    