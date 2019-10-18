"""
-----------------  Laboratorio 1 - Bimestre 1---------------

Autor: @davisalex22

# Ejercicio 5:

Dadas las siguientes edad:
[10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
Se ha generado una lista denomindad black_edades, formada así:
[10, 14, 30, 32, 40, 16]
Generar el listado de edades que no estén dentro de las black_edades.

"""
# Uso de metodo


def com_edades(x):
    # Listado de edades a excluir
    black_edades = [10, 14, 30, 32, 40, 16]
    if x in black_edades:
        return False
    else:
        return True

# Listado general de edades
edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
# Uso de filter para separar el listado de edades a excluir
result = filter(com_edades, edades)
# Muestra en pantalla de resultados
print(list(result))
