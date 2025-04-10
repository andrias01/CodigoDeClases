import time
#_________________________________________
#_________________________________________
#_________________________________________
#_________________________________________
#_________________________________________
#_________________________________________
#_________________________________________
n=8
contador = 0
columna = [False]*n #verifica si la columna ya tiene una reina
diagonal_izq = [False]*(n*2) #verifica si la diagonal izquierda ya tiene una reina
diagonal_der = [False]*(n*2) #verifica si la diagonal derecha ya tiene una reina

def backtrack(y,n,contador): #y es la fila, n es el tamaño del tablero
    if y == n: #si se han colocado todas las reinas
        print("Solucion encontrada")
        return contador+1
    for x in range(n):
        global columnas, diagonal_izq, diagonal_der
        if(columnas[x] or diagonal_izq[x+y] or diagonal_der[x-y+n-1]): #verifica si la columna o la diagonal ya tiene una reina
            continue
        columnas[x] = diagonal_izq[x+y] = diagonal_der[x-y+n-1] = True #coloca la reina
        contador = backtrack(y+1,n,contador)
        columnas[x] = diagonal_izq[x+y] = diagonal_der[x-y+n-1] = False
    return contador
print(backtrack(0,n,contador)) #llama a la funcion backtrack 
print(diagonal_der)
#https://github.com/danielTeniente/guia_de_competencia/blob/master/Backtraking/Algoritmos_recursivos_backtracking.ipynb
#_________________________________________
import random
import time

def imprimir_tablero(tablero):
    print("Estado actual del tablero:")
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else '.' for num in fila))
    print("\n")
    #time.sleep(3)  # Detener la ejecución por 3 segundos

def es_valido(tablero, fila, columna, numero):
    print(f"Verificando si {numero} puede colocarse en la posición ({fila}, {columna})")
    for i in range(9):
        if tablero[fila][i] == numero:
            print(f"{numero} ya está en la fila {fila}")
            return False
        if tablero[i][columna] == numero:
            print(f"{numero} ya está en la columna {columna}")
            return False
    caja_x, caja_y = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(3):
        for j in range(3):
            # print(imprimir_tablero(tablero))
            if tablero[caja_x + i][caja_y + j] == numero:
                print(f"{numero} ya está en la subcuadrícula {caja_x // 3}, {caja_y // 3}")
                return False
    return True

def encontrar_vacio(tablero):
    print("Buscando la siguiente celda vacía...")
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                print(f"Celda vacía encontrada en ({i}, {j})")
                return i, j
    print("No se encontraron celdas vacías, el Sudoku está completo.")
    return None

def resolver(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        imprimir_tablero(tablero)
        print("Sudoku resuelto exitosamente!")
        return True
    fila, columna = vacio
    for numero in range(1, 10):
        if es_valido(tablero, fila, columna, numero):
            print(f"Colocando {numero} en ({fila}, {columna})")
            tablero[fila][columna] = numero
            imprimir_tablero(tablero)
            if resolver(tablero):
                return True
            print(f"Retrocediendo: Eliminando {numero} de ({fila}, {columna})")
            tablero[fila][columna] = 0
    return False

def cargar_tablero():
    print("Cargando el tablero inicial...")
    return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

# Cargar y resolver el tablero
sudoku_tablero = cargar_tablero()
print("Tablero inicial:")
imprimir_tablero(sudoku_tablero)
print("Resolviendo Sudoku paso a paso:")
resolver(sudoku_tablero)
#_________________________________________
def sumDigitos(n,k):
    total = sum(int(digits) for digits in n) * k

    while total >=10:
        total = sum(int(digits) for digits in str(total))
    return print(total)

def sumDigitos(n,k):    
    def super_digito(num):
            if num < 10:
                return num
                #se llama a si misma hasta que el numero es menor a 10
            return super_digito(sum(int(digit) for digit in str(num)))

    # Paso inicial: calcular la suma de los dígitos del número original multiplicado por k
    total2 = sum(int(digit) for digit in n) * k
    #Cuando tengo la suma llamo la funcion super_digito hasta que es menor a 10
    return super_digito(total2)
#_________________________________________
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
##En esta pagina muestra de manera grafica la recursividad https://pythontutor.com/

def factorial1(n,acumulador =1):
    if n == 0:
        return acumulador
    return factorial(n-1, n* acumulador)
factorial1(5)

#_________________________________________
"""
El algoritmo de Dijkstra encuentra el camino más corto entre un nodo dado (el nodo de origen) y todos los otros nodos del grafo. Este algoritmo usa los valores de los arcos para encontrar el camino que minimiza el valor total entre el nodo de origen y los demás nodos del grafo.
"""
#_________________________________________
#O(1) - Tiempo constante    
def acceso_constante(lista):
    return lista[0]  # Acceder al primer elemento siempre toma el mismo tiempo

mi_lista = [10, 20, 30, 40]
print(acceso_constante(mi_lista))  # O(1)

#O(log n) - Tiempo logarítmico
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

mi_lista = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(mi_lista, 7))  # O(log n)

#O(n) - Tiempo lineal
def suma_elementos(lista):
    total = 0
    for numero in lista:
        total += numero  # Recorre toda la lista
    return total

mi_lista = [1, 2, 3, 4, 5]
print(suma_elementos(mi_lista))  # O(n)
#O(n log n) - Tiempo logarítmico lineal
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

mi_lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(merge_sort(mi_lista))  # O(n log n)
#O(n²) - Tiempo cuadrático
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:  # Comparación y posible intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

mi_lista = [5, 3, 8, 4, 2]
print(burbuja(mi_lista))  # O(n²)
#O(2ⁿ) - Tiempo exponencial
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Llamadas recursivas

print(fibonacci(5))  
# O(2ⁿ)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Llamadas recursivas

print(fibonacci(5))  

# O(2ⁿ)
from itertools import permutations

def permutaciones(lista):
    return list(permutations(lista))

mi_lista = [1, 2, 3]
print(permutaciones(mi_lista))  # O(n!)

#_________________________________________
def isPalindrome(self, x):
    x_str = str(x)  # Convertimos el número a string   O(n)
    return x_str == x_str[::-1]  # Comparamos con su versión invertida
"""
str(x) → Convertir un número a una cadena toma O(n) tiempo, donde n es el número de dígitos en x.
x_str[::-1] → Invertir la cadena también toma O(n) tiempo.
Comparación x_str == x_str[::-1] → Comparar dos cadenas de longitud n toma O(n) en el peor caso.
"""
#_____________________________________________________________
class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Si la lista está vacía, retornamos 0
            return 0

        j = 1  # `j` será el puntero para almacenar los valores únicos (comienza en 1)
        
        # Recorremos la lista desde el segundo elemento (i = 1) hasta el final
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Si encontramos un nuevo valor único
                nums[j] = nums[i]  # Guardamos el valor único en la posición j
                j += 1  # Incrementamos `j` para la siguiente posición única
        
        return j  # `j` representa la cantidad de valores únicos en nums
"""
Tiempo (O(n))
La función recorre nums una sola vez en un bucle for, por lo que la complejidad temporal es O(n), donde n es el número de elementos en nums.
Espacio (O(1))
No usamos memoria adicional aparte de unas pocas variables (j, i).
Modificamos nums en su lugar, lo que significa que la complejidad espacial es O(1).
"""
#________________________________________________________________
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Puntero para los elementos que NO son val
        
        # Recorremos la lista
        for i in range(len(nums)):
            if nums[i] != val:  # Si el elemento es diferente de val
                nums[k] = nums[i]  # Lo movemos a la posición k
                k += 1  # Incrementamos k porque encontramos un número válido
        
        return k  # Retornamos la cantidad de elementos que NO son val

# Ejemplo de uso:
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
k = solution.removeElement(nums, val)
print(k, nums[:k])  # Salida esperada: 5, [0,1,3,0,4] (el orden puede variar)
"""
Complejidad Temporal (O(n))
La función tiene un bucle for que itera sobre todos los elementos de nums una vez.
Dentro del bucle, cada elemento se compara con val y, si es diferente, se reasigna en la posición k en nums.
Ambas operaciones (comparación y reasignación) toman O(1) tiempo por elemento.
Dado que recorremos nums una sola vez, la complejidad es O(n), donde n es el número de elementos en nums.
"""
#________________________________________________________________
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []  # Si la entrada está vacía, retornamos una lista vacía
        
        # Mapeo de dígitos a letras (similar a un teclado telefónico)
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []  # Lista para almacenar las combinaciones generadas

        # Función recursiva para generar combinaciones
        def backtrack(index, current_combination):
            if index == len(digits):  # Si alcanzamos la longitud de la entrada, guardamos el resultado
                result.append("".join(current_combination))
                return
            
            current_digit = digits[index]  # Tomamos el dígito actual
            for letter in digit_to_letters[current_digit]:  # Iteramos sobre sus letras correspondientes
                backtrack(index + 1, current_combination + [letter])  # Llamada recursiva con la siguiente letra
        
        # Iniciar el proceso de backtracking desde el primer dígito
        backtrack(0, [])
        return result

# Ejemplo de uso:
solution = Solution()
print(solution.letterCombinations("23"))  
# Salida esperada: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
Tiempo (O(3ⁿ × 4ᵐ))
Cada número genera combinaciones de letras (3 para la mayoría y 4 para el 7 y el 9).
Para un digits de longitud n, la cantidad máxima de combinaciones es 3ⁿ × 4ᵐ, donde m es la cantidad de 7 u 9.
En el peor caso (9999), el tiempo es O(4⁴) = O(256).
Espacio (O(3ⁿ × 4ᵐ))
result almacena todas las combinaciones posibles.
En el peor caso, se guardan O(3ⁿ × 4ᵐ) combinaciones en memoria.
"""
#_________________________________________
#Funcion de serie de fibonacci para practicar una funicion perezosa
#donde se carga toda la serie pero utilizamos solo lo que necesitamos
def getFibonacci():
    yield 0
    a, b = 0,1

    while True:
        yield b
        b= a+b
        a= b-a
fibonaccis = getFibonacci()
print(type(fibonaccis))

print("Primer número",next(fibonaccis))
for num in fibonaccis:
    if num > 500000:
        break
    print("Siguiente número", num)
#_________________________________________
#A. Vanya and Cards ==> de codeForces en "contests"
def min_cards_to_balance(n, x, found_cards):
    total_sum = sum(found_cards)
    
    if total_sum == 0:
        return 0  # Ya está equilibrado
    
    # Se pueden tomar cartas desde -x hasta x, así que verificamos cuántas cartas se necesitan para compensar
    needed_value = abs(total_sum)
    
    # Se necesita al menos una carta con valor igual a 'needed_value' (si existe en el rango)
    if -x <= -total_sum <= x or -x <= total_sum <= x:
        return 1
    
    # Si no se puede con una sola carta, siempre podremos hacerlo con dos como máximo
    return 2

# Lectura de entrada
#n, x = map(int, input().split())
#found_cards = list(map(int, input().split()))

# Cálculo y salida del resultado
#print(min_cards_to_balance(n, x, found_cards))
#__Vanya creado por mi!!
n,x = input().split()
cartasEncontradas = list(map(int,input().split()))

print(n+" - "+x)
print(cartasEncontradas)

def outputCartas():
    print("hoal") 
time.sleep(20)