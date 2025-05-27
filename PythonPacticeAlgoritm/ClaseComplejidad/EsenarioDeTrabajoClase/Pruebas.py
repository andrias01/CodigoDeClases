import heapq
import time

def dijkstra_con_matriz(matriz, origen):
    n = len(matriz)
    distancia = [float('inf')] * n
    predecesor = [None] * n
    distancia[origen] = 0
    visitado = [False] * n

    # Cola de prioridad: (distancia, nodo)
    cola = [(0, origen)]

    while cola:
        dist_u, u = heapq.heappop(cola)
        if visitado[u]:
            continue
        visitado[u] = True

        for v in range(n):
            if u == v:
                continue  # ignorar el mismo nodo
            peso_uv = matriz[u][v]
            nueva_distancia = dist_u + peso_uv
            if nueva_distancia < distancia[v]:
                distancia[v] = nueva_distancia
                predecesor[v] = u
                heapq.heappush(cola, (nueva_distancia, v))

    return distancia, predecesor

# Matriz de adyacencia
matriz = [ 
    [ 0, 34, 56, 12, 78, 90, 43, 67, 23, 55 ],
    [ 34, 0, 64, 21, 12, 44, 90, 13, 45, 66 ],
    [ 56, 64, 0, 50, 34, 33, 76, 82, 28, 59 ],
    [ 12, 21, 50, 0, 22, 88, 16, 44, 73, 10 ],
    [ 78, 12, 34, 22, 0, 25, 90, 17, 65, 33 ],
    [ 90, 44, 33, 88, 25, 0, 14, 56, 32, 71 ],
    [ 43, 90, 76, 16, 90, 14, 0, 36, 48, 11 ],
    [ 67, 13, 82, 44, 17, 56, 36, 0, 20, 24 ],
    [ 23, 45, 28, 73, 65, 32, 48, 20, 0, 60 ],
    [ 55, 66, 59, 10, 33, 71, 11, 24, 60, 0 ]
]

# Ejecutar Dijkstra desde nodo 0
distancia, predecesor = dijkstra_con_matriz(matriz, 0)

# Mostrar suma total de distancias mínimas desde nodo 0
print("Suma de distancias desde nodo 0:", sum(distancia))

# Mostrar predecesores
print("Predecesores:")
for i in range(len(predecesor)):
    print(f"{i} ← {predecesor[i]}")

# Función para reconstruir camino desde origen hasta un destino
def reconstruir_camino(predecesor, destino):
    camino = []
    while destino is not None:
        camino.insert(0, destino)
        destino = predecesor[destino]
    return camino

# Ejemplo: mostrar camino de 0 a 5
destino = 5
camino = reconstruir_camino(predecesor, destino)
print(f"Camino más corto de 0 a {destino}: {camino}")
print(f"Distancia total: {distancia[destino]}")

# Esperar 2 segundos
time.sleep(2000)
