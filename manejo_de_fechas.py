#caracteres especiales
print("imprime:","\\")
print("imprime:","\'")
print("imprime:","\"")
print("imprime:","\n","(salto de linea)")
print("imprime:","\t", "(tabulacion)")
#manejo de fechas y horas
from datetime import date
from datetime import datetime
from datetime import timedelta
#import datetime (importo toda la libreri DE LA OTRA FORMA IMPORTO solo las clases)
epoch_date=56121765
today=date.today()#dia actual esto es un metodo y no una variable
now=datetime.now()#fecha y hora actual
print(today,"\n")
print("Fecha y hora: ",now)
print("el dia actual es: {}".format(today.day))
print("el mes actual es: {}".format(today.month))
print("el dia actual es: {}".format(today.year))
now_epoch = now.timestamp()#toma el instantre detiempo actual lo convierte a segundos 
print("hora now en epoch ()segundos)",now_epoch)
date = datetime.fromtimestamp(epoch_date)
print("Fecha ejemplo de datetime",date)
new_date =datetime(1985, 2, 23, 11, 45, 00, 00000) #defino una fecha insstanciando un feca con el objeto del tipo datetiem(ano, mes dia, hora, min, seg , sentrecimas)#
nacimiento=new_date.strftime('Dia: %d, Mes: %m, Ano: %y')
print(nacimiento)