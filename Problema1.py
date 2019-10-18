"""
-----------------  Laboratorio 1 - Bimestre 1---------------

Autor: @davisalex22

# Ejercicio 1:

Dado el siguiente conjunto de promedios de estudiantes; determinar los estudiantes que pasan de ciclo. 
Todos los estudiantes que pasan de ciclo son aquellos que tienen un promedio de 16.5 o mayor.
promedios.txt
10,20,18,19,20,17,18,16,16,11,12,13
"""

# Lectura de datos
notas = open("promedios.txt")
x = notas.read()
list(x)
y = x.split(",")
# USO DE MAP
y = list(map(int, y))
# USO DE FILTER
result = filter(lambda x: x >= 16.5, y)
# MUESTRA EN PANTALLA
print(list(result))
