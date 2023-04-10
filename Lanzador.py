from Barbero import Barbero
from Cliente import Cliente
from Cola import Cola
import os

def main():

    opcion = 'S'
    cola = Cola()
    barbero = Barbero()
    i = 0
    j = 0

    while opcion == 'S' or opcion == 's':
        os.system('cls')

        if i % 10 == 0:
            opcion = input("Desea agregar un cliente?\n[S/N]\n>>>  ")
            if opcion == 'S' or opcion == 's':
                j += 1
                if cola.estaVacia() or not barbero.isOcupado():
                    cola.encolar(Cliente(j,"Con Barbero"))
                elif cola.count() == 1:
                    cola.encolar(Cliente(j,"Esperando en Silla 1"))