#ejercicio 5: hacer un programa con 1 funcion vacia
#y una funcion que con retorno, para el lanzamiento de
#varios dados. Parametrizar la cantidad de caras de los dados.
#Luego mostrar en pantallael valor que obtuvo en cada dado
#opcional de dific: cojntar las ocurrencias y determinar
#los juegos, Generala, poker, full, escalera, trio, doble par, nada

from random import randint

def intro():
    print("Bienvenido a Generala.py")
    print('Buena Suerte', nombre,'!!!!!')

def lanzar_dado(valor_maximo):
    valor_dado=randint(1,valor_maximo)
    return valor_dado

nombre=input('Como te llamas?: ')
intro()

caras=int(input('Defina el valor de caras:'))

dado_1=int(lanzar_dado(caras))
dado_2=int(lanzar_dado(caras))
dado_3=int(lanzar_dado(caras))
dado_4=int(lanzar_dado(caras))
dado_5=int(lanzar_dado(caras))
dados=[dado_1,dado_2,dado_3,dado_4,dado_5]#lista de dados que me permite jugar conm los valores de los dados mediante alguno de sus metodos

repe_1=dados.count(dado_1)#cuenta cuantas veces aparece el dado 1
repe_2=dados.count(dado_2)#cuenta cuantas veces se aparece el dado 2
repe_3=dados.count(dado_3)#cuenta cuantas veces se aparece el dado 3
repe_4=dados.count(dado_4)#cuenta cuantas veces se aparece el dado 4
repe_5=dados.count(dado_5)#cuenta cuantas veces se aparece el dado 5
repeticiones=[repe_1,repe_2,repe_3,repe_4,repe_5]
match repeticiones:
    case [2,2,1,1,1]:#par
        print('par de ',dado_2)
    case [1,2,2,1,1]:
        print('par de ',dado_3)
    case [1,1,2,2,1]:
        print('par de ',dado_4)    
    case [1,1,1,2,2]:
        print('par de ',dado_5)
    case [2,1,1,1,2]:
        print('par de ',dado_1)
    case [1, 2, 1, 1, 2]:
        print('par de ',dado_2)
    case [1, 2, 1, 2, 1]:
        print('par de ',dado_2)
    case [1, 1, 2, 1, 2]:
        print('par de ',dado_5)

    case [2,2,2,2,1]:#Doble par
        print('Doble Par ')
    case [1,2,2,2,2]:
        print('Doble Par')
    case [2,1,2,2,2]:
        print('Doble Par')
    case [2,2,1,2,2]:
        print('Doble Par')
    case [2,2,2,1,2]:
        print('Doble par')

    case [3,3,3,1,1]:#trio
        print('trio de: ',dado_1)
    case [1,3,3,3,1]:
        print('trio de ',dado_2)
    case [1,1,3,3,3]:
        print('Trio de ',dado_3)
    case [3,1,1,3,3]:
        print('Trio de ',dado_4)
    case [3,3,1,1,3]:
        print('Trio de ',dado_5)
        
    case [3,3,3,2,2]:#Full
        print('Full de: ',dado_1,'y dos',dado_4)
    case [2,3,3,3,2]:
        print('Full de: ',dado_2,'y dos',dado_1)
    case [2,2,3,3,3]:
        print('Full de: ',dado_3,'y dos',dado_2)
    case [3,2,2,3,3]:
        print('Full de: ',dado_4,'y dos',dado_3)
    case [3,3,2,2,3]:
        print('Full de: ',dado_5,'y dos',dado_4)
    
    case [4,4,4,4,1]:#Poker
        print('Poker de: ',dado_1)
    case [1,4,4,4,4]:
        print('Poker de: ',dado_2)
    case [4,1,4,4,4]:  
        print('Poker de: ',dado_3)
    case [4,4,1,4,4]:
        print('Poker de: ',dado_4)
    case [4,4,4,1,4]:
        print('Poker de: ',dado_5)
    
    case [5,5,5,5,5]:#generala
        print('Generala de:',dado_1)
        
    case [1,1,1,1,1]:#Escalera
        if(dado_1>0):
            if(dados==[dado_5-4,dado_5-3,dado_5-2,dado_5-1,dado_5]):
                print('Escalera: ',dados)
    
print('Valor de los dados:',dados)
print('Vepeticion de cada valor',repeticiones)
