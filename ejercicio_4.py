#ejercicio 4
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
edad_dias=timedelta(seconds=fecha_actual_epoch)-timedelta(seconds=fecha_nacimiento_epoch)

anos=int(fecha_actual.strftime('%Y'))-int(fecha_nacimiento.strftime("%Y"))

if(int(fecha_actual.strftime('%m'))<int(fecha_nacimiento.strftime("%m"))):#contempla si los mesesde nacimientoson mayores a los actuales
    anos=anos-1
    meses=int(fecha_nacimiento.strftime("%m"))-int(fecha_actual.strftime('%m'))
    meses=12-meses
meses=int(fecha_actual.strftime('%m'))-int(fecha_nacimiento.strftime("%m"))

if(int(fecha_actual.strftime('%d'))<int(fecha_nacimiento.strftime("%d"))):#contempla si los dias nacimientoson mayores a los actuales
    dias=int(fecha_nacimiento.strftime("%d"))-int(fecha_actual.strftime('%d'))
    meses=meses-1
    dias=30.44-dias
dias=int(fecha_actual.strftime("%d"))-int(fecha_nacimiento.strftime("%d"))

if(int(fecha_actual.strftime('%H'))<int(fecha_nacimiento.strftime("%H"))):#contempla si las nacimientoson mayores a los actuales
    horas=int(fecha_nacimiento.strftime("%H"))-int(fecha_actual.strftime('%H'))
    dias=dias-1
    horas=24-horas
horas=int(fecha_actual.strftime('%H'))-int(fecha_nacimiento.strftime("%H"))  
    
print('Anos:',anos)
print('Meses: ',meses)
print('Dias: ',dias)
print('Horas: ',horas)
print('Minutos: ',minutos)

print('Segundos: ',segundos)
