from random import randint #inporto del modulo random la funcion randint#
numero_jugador_1 = input("Apueste al numero (1 a 6): ")
dado = randint(1,6)
print("Numero del dado 1: ", dado)
if dado==numero_jugador_1:
    print("El Jugador 1 gana")
else:
   print("El Jugador 1 pierde")
numero_jugador_2 = input("Apueste al numero (1 a 6): ")
dado = randint(1,6)
print("Numero del dado 2: ", dado)
if dado==numero_jugador_2:
    print("El Jugador 2 gana")
else:
   print("El Jugador 2 pierde")
   