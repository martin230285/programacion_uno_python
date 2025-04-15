import random

def es_correcto(numero_usuario, numero_secreto):
    if numero_usuario == numero_secreto:#el error estaba en que el operador de comparacion que tenia 
        return True                     #el if era != lo que hacia que siempre sea correcto
    else:
        return False

numero_secreto = random.randint(1, 20)
vidas = 5
print("Estoy pensando en un número entre 1 y 20...")

while(vidas>0):
    vidas=vidas-1
    numero = int(input("Adivina: "))
    if es_correcto(numero, numero_secreto):
        print("Correcto! Adivinaste el número.")
        break
    elif numero < numero_secreto:
        print("Muy bajo.")
    else:
        print("Muy alto.")
if(vidas<=0):
    print("Perdiste! Te quedaste sin vidas")


