#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.

    Parámetros:
    n (int): El número del cual se desea calcular el factorial.

    Retorna:
    int: El factorial de n. Si n es 0, retorna 1 (ya que 0! es 1).
    Para n mayor que 0, retorna n * factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Convertir el argumento de línea de comandos en un entero y calcular el factorial
f = factorial(int(sys.argv[1]))

# Imprimir el resultado
print(f)
