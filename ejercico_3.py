#Realice un programa que genere un numero aleatorio entre 1 y 20.
#Pregunte el nombre del jugador y lo salude. Luego indique
#que tiene 6 vidas para adivinar el numero. Si adivina el numero antes de los 6 intentos, el jugador gana,
#si se queda sin intentos, pierde
from random import randint
intentos = 6
dado = randint(0,20)
print(dado)
nombre = input("como te llamas? ")
print("hola", nombre,",tenes 6 intentos para adivinar el valor del dado")
while intentos>0:
    numero = int(input("Elegi un numero entre 0 y 20: "))
    intentos = intentos-1
    print("restan ", intentos, "intentos")
    if numero==dado:
        print(nombre, ", Ganaste!!!")
        break
if intentos == 0:
    print(nombre,", te quedaste sin intentos")
             