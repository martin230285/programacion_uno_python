# Ejercicio 6:
# A) Un experimento comienza con una bacteria que se duplica cada hora.
# Luego cada una de esas bactrias se duplica al pasar 1 hora. Definir una funcion
# para calcular el numero de bacterias que habra luego de N horas
def calculo_bacteriano(N):
    bacterias=2**N
    return bacterias  
exponente=int(input('Ingresar horas que deben transcurrir:'))
exp=calculo_bacteriano(exponente)
print(calculo_bacteriano(exponente),'bacterias al cabo de,',exponente,'horas')

