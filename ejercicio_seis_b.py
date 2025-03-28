55# # b)Un maestro tiene X cantidad de caramelos y quere repartirlos entre Y cantidad de estudiantes de forma equitativa.
# #defina una funcion que determine cuantos caramelos recibe cada estudiante sin fraccion y que indique cuantos quedan sin repartir

def repartija(estudiantes, caramelos):
    cantidad=caramelos//estudiantes
    resto=caramelos%estudiantes
    resultado=[cantidad, resto]
    return resultado

Alunos=int(input('cantidad de alumnos: '))
Dulces=int(input('Cantidad de caramelos: '))
reparto=repartija(Alunos, Dulces)
print(repartija(Alunos, Dulces))