import time
#______________________________________
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
#____________________ encontrar el numero minimo
lista= [8,9,3,10]
def encontrarMinNumber(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo
resul= encontrarMinNumber(lista)
print(f"El numero minimo de la lista es {resul}")
#_________________

def mediaEstudiantesWithWight(a, b):
    weight_A = 3.5
    weight_B = 7.5
    MEDIA = (a * weight_A + b * weight_B) / (weight_A + weight_B)
    print(f"MEDIA = {MEDIA:.5f}")

def calcular_media(a, b, c):
    # Pesos de las calificaciones
    peso_A = 2
    peso_B = 3
    peso_C = 5

    # Cálculo del promedio ponderado
    media = (a * peso_A + b * peso_B + c * peso_C) / (peso_A + peso_B + peso_C)

    # Imprimir el resultado con el formato exacto
    print(f"MEDIA = {media:.1f}")

# Leer las calificaciones de entrada
A, B, C = map(float, input().split())

# Calcular y mostrar la media
calcular_media(A, B, C)
#mediaEstudiantesWithWight(5.0, 7.1)

# Espera 5 segundos antes de cerrar

#-------------------calse analisis
# Aumentar el límite de recursión
sys.setrecursionlimit(10**6)  # Ajusta según necesites, pero ten cuidado

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def factorial_n(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

n = 5000  # Un número grande para probar

# Medir tiempo recursivo
start = time.time()
try:
    factorial(n)
    print("Factorial recursivo ejecutado correctamente")
except RecursionError:
    print("Error: Se alcanzó el límite de recursión")
end = time.time()
print(f"Recursivo: {end - start:.8f} segundos")

# Medir tiempo iterativo
start = time.time()
factorial_n(n)
end = time.time()
print(f"Iterativo: {end - start:.8f} segundos")

time.sleep(15)
