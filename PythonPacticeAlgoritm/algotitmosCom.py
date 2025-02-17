import time
import os
import sys
"""
12 1 5.30
16 2 5.10

VALOR A PAGAR: R$ 15.50
"""
# Leer los datos del primer producto
codigo1, cantidad1, precio1 = input().split()
codigo1 = int(codigo1)
cantidad1 = int(cantidad1)
precio1 = float(precio1)

# Leer los datos del segundo producto
codigo2, cantidad2, precio2 = input().split()
codigo2 = int(codigo2)
cantidad2 = int(cantidad2)
precio2 = float(precio2)

# Calcular el valor total a pagar
total = (cantidad1 * precio1) + (cantidad2 * precio2)

# Imprimir el resultado con el formato requerido
print(f"VALOR A PAGAR: R$ {total:.2f}")




time.sleep(15)
