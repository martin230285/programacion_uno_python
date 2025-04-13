# En un bosque encantado un explorador llega a una bifurcacion donde el sendero se abre en dos. Uno de los 
# senderos lleva a la guardia de un unicornio blanco que le concede umn deseo (ganar el juego) y en el otro 
# sendero hay un minotauro furioso (pierde). Ademas al comenzar el juego tiene un 50% de porobabilidad de 
# encontrar un amuleto magico, que le permita detener el tiempo y escapar de situaciones peligrosas (no pierde aunque elija mal)
# 1) Definir al menos dos funciones: una (vacia) una para mostrar la introduccion y la otra para elegir el sendero y
#  retornarlo
# 2) Utilizar time.sleep(2) para hacer pausa dramatica
# 3) Aplicar operadores logicos(and, or, not) en las desiciones
# 4) Usar random.randint(0,1) 0 randon.choice([True, False]) para decidir si el jugador tiene un objeto especial
#  que lo proteja
import time 
import random


explorador=input('Como te llamads explorador: ')
def intro ():
    print('En un bosque encantado',explorador,'llega a una bifurcacion en donde el sendero se abre en dos...')
    time.sleep(3)
    print('Cuidado', explorador, end='!!!!!\n')
    print('Uno de los senderos es custodiado por un MINOTAURO MALVADO que aniquila a todo aquel que quiera pasar por alli')
    print('El otro sendero es vigilado por un UNICORNIO BLANCO que le concede un deseo a los exploradores que toman ese camino')

def sendero(bifurcacion):
    minotauro=random.randint(1,2)
    posee_escudo=[True,False]
    escudo_magico=random.choice(posee_escudo)
    valores=[minotauro,escudo_magico]
    return valores
   
intro()
while (True):
    eleccion=int(input('cual sendero te  llevara a la victoria? (sendero 1 o sendero 2): '))
    echada_la_suerte=sendero(eleccion)
    if(echada_la_suerte[0]==eleccion and echada_la_suerte[1]==False):
        print(explorador,'te has encontrado con el Minotauro enfurecido')
        print('Cuidadoo!!!\n')
        print('el minotauro no te ha perdonado,',explorador,'has perdido el juego')
    if (echada_la_suerte[0]==eleccion and echada_la_suerte[1]==True):
        print(explorador,'te as encontrado con el minotauro!!!')
        print('Cuindadoooo!!!!')
        time.sleep(3)
        print('Un escudo magico te a rodeado permitiendote escapar')
        print('Felicitaciones has ganado el juego!!')
    if(echada_la_suerte[0]!=eleccion):
        print(explorador,'Tu sendero es el custodiado pr el UNICORNIO BLANCO!!!\n')
        print('podras pedirle un deseo y seguir tu camino. HAS GANADO EL JUEGO')