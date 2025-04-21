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
print(promedio) 
print('original', notas_juan)
#item b
def notas(juan):
      if juan[0]>juan[1]:
            valor=juan[1]
            juan.insert(1, juan[0])
            juan.insert(0, valor)
            juan.pop(2)
            juan.pop(2)

      if juan[1]>juan[2]:
            valor=juan[2]
            juan.insert(2, juan[1])
            juan.insert(1, valor)
            juan.pop(3)
            juan.pop(3)
      
      if juan[2]>juan[3]:
            valor=juan[3]
            juan.insert(3, juan[2])
            juan.insert(2, valor)
            juan.pop(4)
            juan.pop(4)
       
      if juan[3]>juan[4]:
            valor=juan[4]
            juan.insert(4, juan[3])
            juan.insert(3, valor)
            juan.pop(5)
            juan.pop(5)

      if juan[4]>juan[5]:
            valor=juan[5]
            juan.insert(5, juan[4])
            juan.insert(4, valor)
            juan.pop(6)
            juan.pop(6)
      
      if juan[5]>juan[6]:
            valor=juan[6]
            juan.insert(6, juan[5])
            juan.insert(1, valor)
            juan.pop(7)
            juan.pop(7)
      
      if juan[6]>juan[7]:
            valor=juan[7]
            juan.insert(7, juan[6])
            juan.insert(6, valor)
            juan.pop(8)
            juan.pop(8)

      return juan
while (i<8):
      valores = notas(notas_juan)
      i+=1
print('modifica',valores)
