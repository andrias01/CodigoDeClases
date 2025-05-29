"""
ALGORITMO DE DIJKSTRA - ADAPTADO PARA MATRIZ DE ADYACENCIA

PROBLEMA: Encontrar el camino más corto desde un nodo origen a todos los demás nodos
en un grafo representado como matriz de adyacencia con pesos no negativos.

PRINCIPIO: Algoritmo greedy que siempre selecciona el nodo no visitado con menor distancia.

APLICACIONES:
- Sistemas de navegación GPS
- Redes de computadoras
- Planificación de rutas
- Análisis de redes sociales

COMPLEJIDAD: O(V²) para implementación con matriz de adyacencia
"""

import heapq

class GrafoMatriz:
    def __init__(self, matriz_adyacencia):
        """
        Inicializa un grafo a partir de una matriz de adyacencia.
        
        Args:
            matriz_adyacencia: Lista de listas representando la matriz de adyacencia.
                              Un valor de 0 indica que no hay conexión directa.
        """
        self.matriz = matriz_adyacencia
        self.num_nodos = len(matriz_adyacencia)
        
        # Validar que la matriz sea cuadrada
        for fila in matriz_adyacencia:
            if len(fila) != self.num_nodos:
                raise ValueError("La matriz de adyacencia debe ser cuadrada")
    
    def dijkstra(self, origen):
        """
        Ejecuta el algoritmo de Dijkstra desde un nodo origen.
        
        Args:
            origen: Índice del nodo desde donde comenzar la búsqueda (0 a n-1)
            
        Returns:
            (distancias, predecesores) donde:
            - distancias: lista con la distancia mínima a cada nodo
            - predecesores: lista para reconstruir los caminos
        """
        if origen < 0 or origen >= self.num_nodos:
            raise ValueError(f"El nodo origen {origen} está fuera del rango válido (0-{self.num_nodos-1})")
        
        # Inicializar distancias y predecesores
        distancias = [float('infinity')] * self.num_nodos
        predecesores = [None] * self.num_nodos
        distancias[origen] = 0
        
        # Lista para marcar nodos visitados
        visitados = [False] * self.num_nodos
        
        # Cola de prioridad: (distancia, nodo)
        cola_prioridad = [(0, origen)]
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            # Si ya visitamos este nodo, continuar
            if visitados[nodo_actual]:
                continue
            
            # Marcar como visitado
            visitados[nodo_actual] = True
            
            # Examinar todos los vecinos
            for vecino in range(self.num_nodos):
                peso = self.matriz[nodo_actual][vecino]
                
                # Si hay una conexión (peso > 0) y el vecino no ha sido visitado
                if peso > 0 and not visitados[vecino]:
                    nueva_distancia = distancia_actual + peso
                    
                    # Si encontramos un camino más corto
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        predecesores[vecino] = nodo_actual
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
        
        return distancias, predecesores
    
    def obtener_camino(self, predecesores, origen, destino):
        """
        Reconstruye el camino más corto entre origen y destino.
        
        Args:
            predecesores: Lista de predecesores de dijkstra
            origen: Nodo origen
            destino: Nodo destino
            
        Returns:
            Lista con el camino más corto, o None si no hay camino
        """
        if predecesores[destino] is None and destino != origen:
            return None  # No hay camino
        
        camino = []
        nodo_actual = destino
        
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = predecesores[nodo_actual]
        
        camino.reverse()
        return camino
    
    def imprimir_resultado(self, origen, distancias, predecesores):
        """Imprime los resultados del algoritmo de Dijkstra de forma legible."""
        print(f"\nResultados del algoritmo de Dijkstra desde el nodo {origen}:")
        print("-" * 60)
        
        for nodo in range(self.num_nodos):
            if distancias[nodo] == float('infinity'):
                print(f"Nodo {origen} → Nodo {nodo}: No hay camino")
            else:
                camino = self.obtener_camino(predecesores, origen, nodo)
                camino_str = " → ".join(map(str, camino))
                print(f"Nodo {origen} → Nodo {nodo}: distancia = {distancias[nodo]:3}, camino = {camino_str}")
    
    def imprimir_matriz(self):
        """Imprime la matriz de adyacencia de forma legible."""
        print("Matriz de adyacencia:")
        print("   ", end="")
        for i in range(self.num_nodos):
            print(f"{i:3}", end=" ")
        print()
        
        for i in range(self.num_nodos):
            print(f"{i}: ", end="")
            for j in range(self.num_nodos):
                print(f"{self.matriz[i][j]:3}", end=" ")
            print()
        print()

# Ejemplo de uso con tu grafo
if __name__ == "__main__":
    # Tu matriz de adyacencia
    grafo = [
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
    
    # Crear el grafo
    g = GrafoMatriz(grafo)
    
    # Mostrar la matriz
    g.imprimir_matriz()
    
    # Ejecutar Dijkstra desde el nodo 0
    nodo_origen = 0
    distancias, predecesores = g.dijkstra(nodo_origen)
    
    # Mostrar resultados
    g.imprimir_resultado(nodo_origen, distancias, predecesores)
    
    # Ejemplos específicos de caminos más cortos
    print("\nEjemplos de caminos específicos:")
    print("=" * 40)
    
    destinos_ejemplo = [3, 6, 9]
    for destino in destinos_ejemplo:
        camino = g.obtener_camino(predecesores, nodo_origen, destino)
        if camino:
            print(f"Camino más corto del nodo {nodo_origen} al nodo {destino}:")
            print(f"  Ruta: {' → '.join(map(str, camino))}")
            print(f"  Distancia total: {distancias[destino]}")
        else:
            print(f"No hay camino del nodo {nodo_origen} al nodo {destino}")
        print()
    
    # Función para probar diferentes orígenes
    def probar_diferentes_origenes():
        print("\nProbando desde diferentes nodos origen:")
        print("=" * 50)
        
        for origen in [0, 4, 7]:
            print(f"\nDesde nodo {origen}:")
            dist, pred = g.dijkstra(origen)
            
            # Mostrar solo las 3 distancias más cortas (excluyendo el origen)
            distancias_ordenadas = sorted([(d, i) for i, d in enumerate(dist) if i != origen and d != float('infinity')])[:3]
            
            for distancia, nodo in distancias_ordenadas:
                camino = g.obtener_camino(pred, origen, nodo)
                print(f"  → Nodo {nodo}: distancia {distancia}, ruta: {' → '.join(map(str, camino))}")
    
    # Ejecutar la prueba adicional
    probar_diferentes_origenes()