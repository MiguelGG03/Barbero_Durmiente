# Barbero Durmiente

El enlace al repositorio es el siguiente : [GitHub](https://github.com/migueliiin/Barbero_Durmiente.git)

## Problema

El problema del barbero es que es un barbero con tres sillas y va a atender a n clientes, y cuando el barbero no tiene clientes se acuesta a dormir

## Resolucion

He creado tres clases: una de tipo Cola para gestionar la cola de los clientes, otra clase de tipo Cliente para poder almacenar el tiempo esperado y a esperar de cada cliente, además de para saber si se estan cortando el pelo o esperando, y una clase Barbero solamente para saber si esta trabaando o no.

El programa original funciona de la siguiente manera:

Se inicializan los objetos a utilizar y las variables que almacenan el numero de cliente y la hora a la que se inicia el programa ( que ese irá actualizando ) la cual usamos para medir tiempos , esta esencialmente vale para medir el primer tiempo, nada más.

Después, dependiendo del caso en el que se encuentre la barbería, entrarán clientes o no, si intenta entrar un cliente se suma 1 al contador de clientes, si ve que la barbería está llena se sale y se resta 1 al contador.

Por último, el programa comprobará si la cola está vacia, es decir, que no hay clientes en la barbería, si no los hay pues el barbero dormirá, y en el caso contrario es que hay cientes. Si hay clientes se comprobará si el tiempo de espera <= a el tiempo esperado, si es así el cliente sale y la cola se mueve, si no cumple el tiempo esperado se le añade a su tiempo esperado el tiempo que ya ha esperado más el tiempo que marque un contador que está atento a cuanto tiempo tarda el usuario en decir que entre otro cliente ( tiempo real ).

## Errores

>No he conseguido librarme de el siguiente error:

Cuando el programa está siendo ejecutado con dos o más clientes, el tiempo esperado que se añade, por alguna razón no es solo añadido al cliente que está con el barbero, sino que también se le añade al cliente que esté sentado en la silla 1 ( el siguiente cliente a cortar el pelo ).

## Posibles soluciones

>No estoy seguro de que esto fuera a funcionar:

Realizar el programa con hilos o multiprocesos ( con pipes para poder utilizar la información de ambos procesos ), donde los hilos servirían para ejecutar el programa por un lado y llevar el contador de tiempo por otro, de tal manera que no hiciera falta interactuar con la maquina para que ella supiera que tiene que mover a los clientes de la cola.
