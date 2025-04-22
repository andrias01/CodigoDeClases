import time
import random

# Parámetros generales
N = 8  # Tamaño del tablero y número de reinas
POBLACION_INICIAL = 400
GENERACIONES = 500
PROB_MUTACION = 0.01

# --------------------------------------
# Función de evaluación (fitness)
# --------------------------------------

def calcular_ataques(tablero):
    ataques = 0
    for i in range(N):
        for j in range(i + 1, N):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return ataques
   
# --------------------------------------
# Generar una solución aleatoria (una reina por columna, fila aleatoria)
# --------------------------------------

def crear_individuo():
    return [random.randint(0, N - 1) for _ in range(N)]

# --------------------------------------
# Selección por torneo: selecciona al mejor de dos individuos aleatorios
# --------------------------------------

def seleccion(poblacion):
    mejor = random.choice(poblacion)
    oponente = random.choice(poblacion)
    return mejor if calcular_ataques(mejor) < calcular_ataques(oponente) else oponente

# --------------------------------------
# Cruce de un punto
# --------------------------------------

def cruzar(padre1, padre2):
    punto = random.randint(1, N - 2)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

# --------------------------------------
# Mutación: cambia una reina a otra fila aleatoria
# --------------------------------------

def mutar(individuo):
    if random.random() < PROB_MUTACION:
        i = random.randint(0, N - 1)
        individuo[i] = random.randint(0, N - 1)
    return individuo

# --------------------------------------
# Algoritmo Genético principal
# --------------------------------------

def algoritmo_genetico():
    poblacion = [crear_individuo() for _ in range(POBLACION_INICIAL)]
    for generacion in range(GENERACIONES):
        poblacion.sort(key=calcular_ataques)
        mejor = poblacion[0]
        if calcular_ataques(mejor) == 0:
            print(f"\n¡Solución encontrada en la generación {generacion}!")
            return mejor

        nueva_poblacion = []
        while len(nueva_poblacion) < POBLACION_INICIAL:
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    print("\nNo se encontró una solución perfecta.")
    return poblacion[0]

# --------------------------------------
# Ejecutar
# --------------------------------------

solucion = algoritmo_genetico()

print("\nCromosoma ganador (solución):")
print(solucion)
print(f"\nNúmero de ataques: {calcular_ataques(solucion)}")

print("\nTablero (modo texto):")
for fila in range(N):
    linea = ""
    for col in range(N):
        if solucion[col] == fila:
            linea += " Q "
        else:
            linea += " . "
    print(linea)
# poblacionPrueba = [crear_individuo() for _ in range(POBLACION_INICIAL)]
# print("Población inicial:")
# for i in range(POBLACION_INICIAL):
#     print(poblacionPrueba[i])

# poblacionPrueba.sort(key=calcular_ataques)
# print("\nPoblación ordenada por ataques:")
# for i in range(POBLACION_INICIAL):
#     print(f"{poblacionPrueba[i]} +  - Ataques:  + {str(calcular_ataques(poblacionPrueba[i]))}")


# padre1 = seleccion(poblacionPrueba)
# padre2 = seleccion(poblacionPrueba)
# print(f"\nPadre 1: {padre1} - Ataques: {str(calcular_ataques(padre1))}")
# print(f"Padre 2: {padre2} - Ataques: {str(calcular_ataques(padre2))}")

# hijo = cruzar(padre1, padre2)
# print(f"\nHijo: {hijo} - Ataques: {str(calcular_ataques(hijo))}")

# print(random.random())

# hijoMutado = mutar(hijo)
# print(f"\nHijo mutado: {hijoMutado} - Ataques: {str(calcular_ataques(hijoMutado))}")
time.sleep(200)


