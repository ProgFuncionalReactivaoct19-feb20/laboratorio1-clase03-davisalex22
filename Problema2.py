"""
-----------------  Laboratorio 1 - Bimestre 1---------------

Autor: @davisalex22

# Ejercicio 2:
Dada la siguiente lista:
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
En contrar una lista como sigue:
[20, 16, 20, 15]
"""
# Lista
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

# Uso de lambda
def suma(x): return x[0] + x[1] + x[2]

# Muestra de resultados por pantallas
print(list(map(suma, notas)))
