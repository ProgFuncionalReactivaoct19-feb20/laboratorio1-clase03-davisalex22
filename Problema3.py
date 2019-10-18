"""
-----------------  Laboratorio 1 - Bimestre 1---------------

Autor: @davisalex22

# Ejercicio 3:
Dada la siguiente frase:

"No hay medicina que cure lo que no cura la felicidad"

Encuentre el listado que sigue:

["No", "hay", "que", "lo", "que", "no", "la"]

"""
# Frase dada por el problema
frase = "No hay medicina que cure lo que no cura la felicidad"

# Uso de split que convierte una cadena de texto en una lista y funcion filter y lambda
result = filter(lambda x: len(x) <= 3, frase.split(" "))

# Muestra en pantalla de resultado
print(list(result))
