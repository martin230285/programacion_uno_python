from random import randint
def lanzar_dado(valor_max):
    #nombre(parametro):
    valor_dado = randint(1,valor_max)
    return valor_dado #retorna el resultado del la operacion querealiza l funcion
cara=int(input('Elija el numero de caras: '))
lanzamiento = lanzar_dado(cara)
print('Lanzo un dado de ', cara,'obtiene: ', lanzar_dado(cara))