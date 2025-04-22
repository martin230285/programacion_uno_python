#los estudiantyes a lo largo del año tiene 8 calificasiones. Las de juan son: 4,2,5,9,9,8.5,7,8
#a)Calcular el promedio de sus notas.
#b)Ordenar la lista de menor a mayor. No usar el metodo sort().
notas_juan=[4, 2, 5, 9, 9 , 8.5, 7, 8]
i = 0 
suma = 0
#Item a:
for elemento in notas_juan:
   suma += elemento
promedio = (suma)/8
print('Promedio: ',promedio) 
print('original', notas_juan)
#item b
n_notas=len(notas_juan)
for j in range(0,n_notas):
    for i in range(0,n_notas-1):
        if notas_juan[i]>notas_juan[i+1]:
            permutador=notas_juan[i+1]
            notas_juan[i+1]=notas_juan[i]
            notas_juan[i]=permutador

print('Notas ordenadas: ', notas_juan)
