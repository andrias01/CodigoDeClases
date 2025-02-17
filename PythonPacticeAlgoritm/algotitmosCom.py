import time
import os
import sys

lista = ["314", "1", "3", "10", "3", "5"]

def bigSorting(unsorted):
    n = len(unsorted) #define numero de la longitud de la lista
    print(f"La longitud de la lista es {n}")
    
    # Implementación de Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            ##print(f"lugar {i} valor = {}")
            # Comparamos los elementos según la longitud y luego lexicográficamente
            if len(unsorted[j]) > len(unsorted[j + 1]) or \
               (len(unsorted[j]) == len(unsorted[j + 1]) and unsorted[j] > unsorted[j + 1]):
                # Intercambiamos si el orden es incorrecto
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted

print(f"la lista ordenada es {bigSorting(lista)}")


time.sleep(15)
