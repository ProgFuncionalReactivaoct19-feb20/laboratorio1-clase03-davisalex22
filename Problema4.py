"""
-----------------  Laboratorio 1 - Bimestre 1---------------

Autor: @davisalex22

# Ejercicio 4:

Dado el siguiente listado:

notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

Filtrar aquellos que tiene la calificación cualitativa "Regular o Bueno"
"""

# Listado
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"),
         (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

# Uso de funcion filter y lambda para filtrar resultatos en la posicion x[3]
resultado = filter(lambda x: x[3] == "Regular" or x[3] == "Bueno", notas)

# Muestra en pantalla de resultado
print(list(resultado))
