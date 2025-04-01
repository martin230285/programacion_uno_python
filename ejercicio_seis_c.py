#ejercicio 6
# c) Un cajero automatico solo entrega billetes de 1000. Definir una funcion que segun el monto que quiere extraer el usuario,
# indiquecuantos billetes debe entregar y cuanto dinero sobra sin poder extraerse.
# opcional de dificultad: suponer que el cajero puede entregar billetes de $2000, $1000 y $500dos_mil=1000 #el unmero indica la cantidad de billetes de que hay en el cajero el nombre de la variable es el valor nominal del billete


billete_mil=2000 #el unmero indica la cantidad de billetes de que hay en el cajero el nombre de la variable es el valor nominal del billete
condicion=True

def cajero_mil(monto_retiro):
    monto_cajero=billete_mil*1000
    entrega=monto_retiro//1000#division exacta
    saldo=monto_retiro%1000#resti division
    entrega=entrega*1000

    if(monto_cajero<=0):
        print('Cajero sin dinero')
        condicion=False
    if(monto_cajero<monto_retiro):
        condicio=False
    
    detalle=[entrega, saldo]
    return detalle

while(condicion):  
    retiro=int(input('ingrese un monto(minimo 1000): '))
    monto=cajero_mil(retiro)
    
    ret=monto[0]
    sal=monto[1]
    billete_mil=billete_mil-(ret/1000)
    
    if(sal!=0):
        print('El cajero soloentrega multipolos de 1000',end='\n')
        deside=int(input('Desea elegir otro importe(1=si/2=no)'))
        match (deside):
            case 1:
                retiro=int(0)
                ret=0
                sal=0
            case 2:
               print('Usted retira $',ret)
               print('Vuelve a cuenta $',sal) 

    print('Usted retira $',ret)
    print('Vuelve a cuenta $',sal)
    print('Dinero en el cajero$',billete_mil*1000)

if(monto_cajero<monto_retiro):
    print('El cajero no tiene saldo disponible')
    condicio=True


       
 
    
