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
    
    def encolar(self, item:Cliente):
        """ Metodo que agrega un cliente a la cola como último elemento """
        self.items.append(item)

    def first(self):
        """ Metodo que devuelve el primer elemento de la cola """
        try:
            self.items[0]
        except IndexError:
            print("La cola esta vacia")

    def desencolar(self):
        """ Metodo que elimina el primer elemento de la cola """
        try:
            self.items.pop(0)
        except IndexError:
            print("La cola esta vacia")

    def tamano(self):
        """ Metodo que devuelve el tamaño de la cola """
        return len(self.items)
    
    def imprimir(self):
        """ Metodo que imprime la cola """
        try:
            self.items[0]
            self.items[1]
            self.items[2]
            self.items[3]

            print(f"[ Cliente {self.items[0].getNumCliente()} - {self.items[0].getEstado()} , Cliente {self.items[1].getNumCliente()} - {self.items[1].getEstado()} , Cliente {self.items[2].getNumCliente()} - {self.items[2].getEstado()} - Cliente {self.items[3].getNumCliente()} - {self.items[3].getEstado()} ]")
        except IndexError:
            try:
                self.items[0]
                self.items[1]
                self.items[2]

                print(f"[ Cliente {self.items[0].getNumCliente()} - {self.items[0].getEstado()} , Cliente {self.items[1].getNumCliente()} - {self.items[1].getEstado()} , Cliente {self.items[2].getNumCliente()} - {self.items[2].getEstado()} , Silla 3 - Vacio ]")
            except IndexError:
                try:
                    self.items[0]
                    self.items[1]

                    print(f"[ Cliente {self.items[0].getNumCliente()} - {self.item[0].getEstado()}, Cliente {self.items[1].getNumCliente()} - {self.item[1].getEstado()} , Silla 2 - Vacio , Silla 3 - Vacio ]")
                except IndexError:
                    try:
                        self.items[0]

                        print(f"[ Cliente {self.items[0].getNumCliente()} - {self.item[0].getEstado()} , Silla 2 - Vacio , Silla 3 - Vacio ]")
                    except IndexError:
                        print("[ Nadie con Barbero , Silla 1 - Vacio , Silla 2 - Vacio , Silla 3 - Vacio ]")

    def count(self):
        """ Metodo que devuelve el numero de clientes en la cola """
        return len(self.items)
    
    def estaVacia(self):
        """ Metodo que verifica si la cola esta vacia """
        return self.items == []

    