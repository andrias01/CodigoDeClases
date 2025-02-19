import time
#PROBLEMA 1014
#______________________________________
#PROBLEMA 1013
#______________________________________
#PROBLEMA 1012
#______________________________________
#PROBLEMA 1011
R = int(input())
pi = 3.14159
formula = (4/3)*pi*(R**3)

print(f"VOLUME = {formula:.3f}")
#______________________________________
#PROBLEMA 1010
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

#______________________________________
#PROBLEMA 1009
employeName = (input())  
salary = float(input())  
sales = float(input())   

salaryCostbySales = (sales*(15/100))+salary

print(f"TOTAL = R$ {salaryCostbySales:.2f}")
#______________________________________
#PROBLEMA 1008
# Leer los valores de entrada
numero_empleado = int(input())  # Número del empleado
horas_trabajadas = int(input())  # Horas trabajadas en el mes
pago_por_hora = float(input())  # Pago por hora trabajada

# Calcular el salario
salario = horas_trabajadas * pago_por_hora

# Imprimir el resultado con el formato requerido
print(f"NUMBER = {numero_empleado}")
print(f"SALARY = U$ {salario:.2f}")

#______________________________________
#PROBLEMA 1007
# Leer cuatro valores enteros desde la entrada
A = int(input())  
B = int(input())  
C = int(input())  
D = int(input())  

# Calcular la diferencia de los productos
DIFERENCA = (A * B) - (C * D)

# Imprimir el resultado con el formato correcto
print(f"DIFERENCA = {DIFERENCA}")

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
##sys.setrecursionlimit(10**6)  # Ajusta según necesites, pero ten cuidado

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
