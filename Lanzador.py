from Barbero import Barbero
from Cliente import Cliente
from Cola import Cola
import os
import time

def main():

    opcion = 'S'
    cola = Cola()
    barbero = Barbero()
    i = 0
    j = 0

    hora=time.time()
    os.system('cls')
    while opcion == 'S' or opcion == 's':


        if i % 10 == 0:
            opcion = input("Desea agregar un cliente?\n[S/N]\n>>>  ")
            hora_desp=time.time()-hora
            hora=time.time()
            if opcion == 'S' or opcion == 's':
                j += 1
                if cola.estaVacia():
                    cola.encolar(Cliente(j,"Con Barbero"))
                elif cola.count() == 1:
                    cola.encolar(Cliente(j,"Esperando en Silla 1"))
                elif cola.count() == 2:
                    cola.encolar(Cliente(j,"Esperando en Silla 2"))
                elif cola.count() == 3:
                    cola.encolar(Cliente(j,"Esperando en Silla 3"))
                else:
                    print("No hay sillas disponibles, el cliente se va\n")
                    j -= 1

            print("| Posiciones totales : [ Barbero , Silla 1 , Silla 2 , Silla 3 ] |\n")
            print("---------------------------------------------------------------\n")
            print(f"| Posiciones ocupadas : {cola.imprimir()} |\n")

        if not cola.estaVacia():
            cliente_1=cola.first()
            if cliente_1.getTiempoDeEspera() == cliente_1.getTiempoEsperado():
                cola.desencolar()
                print("Salio un cliente de la cola\n")
                if not cola.estaVacia():
                    cliente_1.setEstado("Con Barbero")
                    barbero.setOcupado(True)
                else:
                    barbero.setOcupado(False)
                k = 0
                for item in cola.items:
                    if not k == 0:
                        item.setEstado(f"Esperando en Silla {k}")
                    k += 1
                print("| Posiciones totales: [ Barbero , Silla 1 , Silla 2 , Silla 3 ] |\n")
                print("---------------------------------------------------------------\n")
                print(f"| Posiciones ocupadas: {cola.imprimir()} |\n")
            else:
                cliente_1.setTiempoEsperado(cliente_1.getTiempoEsperado() + int(round((hora_desp),0)))
        i += 1

if __name__ == "__main__":
    main()