23#ejercicio 4
#Hacer un programaque le pregunten al usuario su nombre
#fecha de nacimiento y luego indicar la edad en dos formatos
# a) edad en dias
#b)edad en años (años, mes, dias, horas, minutosy segundos=)
#ademas, mostrar en pantalla su fecha de nacimiento y la fecha actual en formato epoch (o timestamp)}
from datetime import date
from datetime import datetime
from datetime import timedelta

#lo que pide el programa
#nombre=input('Ingrese su nombre: ')
#apellido=input('Ingrese su apellido: ')
dia=int(input('Ingresar dia de nacimiento (dd): '))
mes=int(input('Ingresar mes de nacimiento (mm): '))
año=int(input('Ingresar año de nacimiento (aa): '))
hora=int(input('Ingresar hora de nacimiento (hs): '))
minutos=int(input('Ingresar minutos de nacimiento (mi): '))
segundos=int(input('Ingresar año de nacimiento (se): '))

#calculos previos
fecha_actual=datetime.now()#fecha(ano-mes-dia) y hora actual(hs-min-seg.decimas)
f_actual=fecha_actual.strftime('Dia: %d, Mes: %m, Año: %y, Hora: %H, Minutos: %M, Segundos: %S')
fecha_nacimiento=datetime(año, mes , dia, hora, minutos, segundos, 00000)
nacimiento=fecha_nacimiento.strftime('Dia: %d, Mes: %m, Año: %y, Hora: %H, Minutos: %M, Segundos: %S')

fecha_actual_epoch = fecha_actual.timestamp()
fecha_nacimiento_epoch = fecha_nacimiento.timestamp()
edad_segundos=fecha_actual_epoch-fecha_nacimiento_epoch

anos=int(fecha_actual.strftime('%Y'))-int(fecha_nacimiento.strftime("%Y"))

minutos_enteros=edad_segundos//60 
edad_seg=edad_segundos%60 #segundos que tengo de edad

horas_enteras=minutos_enteros//60
minutos=minutos_enteros%60

dias_enteros=horas_enteras//24
horas=horas_enteras%24

meses_enteros=dias_enteros//(365.25/12)
dias=(dias_enteros%(365.25/13))//1

anos=dias_enteros//365.25
meses=(dias_enteros%365.25)//24

edad=[anos,'años',meses,'meses',dias,'dias',horas,'horas',minutos,'minutos',edad_seg,'segundos']
print('Su edad es: ',edad)