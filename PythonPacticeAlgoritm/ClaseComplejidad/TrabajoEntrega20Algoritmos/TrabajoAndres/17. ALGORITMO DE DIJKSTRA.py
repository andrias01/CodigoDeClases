"""
PROBLEMA: Encontrar el camino más corto desde un nodo origen a todos los demás nodos
en un grafo dirigido con pesos no negativos.

PRINCIPIO: Algoritmo greedy que siempre selecciona el nodo no visitado con menor distancia.

APLICACIONES:
- Sistemas de navegación GPS
- Redes de computadoras
- Planificación de rutas
- Análisis de redes sociales

COMPLEJIDAD: O((V + E) log V) con heap, O(V²) con array simple

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
"""

import heapq
from collections import defaultdict, deque

class Grafo:
    def __init__(self):
        """Inicializa un grafo dirigido con pesos."""
        self.grafo = defaultdict(list)
        self.nodos = set()
    
    def agregar_arista(self, desde, hacia, peso):
        """
        Agrega una arista dirigida al grafo.
        
        Args:
            desde: Nodo origen
            hacia: Nodo destino  
            peso: Peso de la arista (debe ser no negativo)
        """
        if peso < 0:
            raise ValueError("El algoritmo de Dijkstra no funciona con pesos negativos")
        
        self.grafo[desde].append((hacia, peso))
        self.nodos.add(desde)
        self.nodos.add(hacia)
    
    def dijkstra(self, origen):
        """
        Ejecuta el algoritmo de Dijkstra desde un nodo origen.
        
        Args:
            origen: Nodo desde donde comenzar la búsqueda
            
        Returns:
            (distancias, predecesores) donde:
            - distancias: dict con la distancia mínima a cada nodo
            - predecesores: dict para reconstruir los caminos
        """
        if origen not in self.nodos:
            raise ValueError(f"El nodo {origen} no existe en el grafo")
        
        # Inicializar distancias y predecesores
        distancias = {nodo: float('infinity') for nodo in self.nodos}
        predecesores = {nodo: None for nodo in self.nodos}
        distancias[origen] = 0
        
        # Cola de prioridad: (distancia, nodo)
        cola_prioridad = [(0, origen)]
        visitados = set()
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            # Si ya visitamos este nodo, continuar
            if nodo_actual in visitados:
                continue
            
            # Marcar como visitado
            visitados.add(nodo_actual)
            
            # Examinar todos los vecinos
            for vecino, peso in self.grafo[nodo_actual]:
                if vecino not in visitados:
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
            predecesores: Diccionario de predecesores de dijkstra
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
        print(f"\nResultados del algoritmo de Dijkstra desde '{origen}':")
        print("-" * 50)
        
        for nodo in sorted(self.nodos):
            if distancias[nodo] == float('infinity'):
                print(f"{origen} → {nodo}: No hay camino")
            else:
                camino = self.obtener_camino(predecesores, origen, nodo)
                camino_str = " → ".join(map(str, camino))
                print(f"{origen} → {nodo}: distancia = {distancias[nodo]}, camino = {camino_str}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un grafo de ejemplo
    g = Grafo()
    
    # Agregar aristas: (desde, hacia, peso)
    aristas = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    print("Construyendo grafo con las siguientes aristas:")
    for desde, hacia, peso in aristas:
        g.agregar_arista(desde, hacia, peso)
        print(f"  {desde} → {hacia} (peso: {peso})")
    
    # Ejecutar Dijkstra desde el nodo 'A'
    nodo_origen = 'A'
    distancias, predecesores = g.dijkstra(nodo_origen)
    
    # Mostrar resultados
    g.imprimir_resultado(nodo_origen, distancias, predecesores)
    
    # Ejemplo específico: camino más corto de A a F
    camino_af = g.obtener_camino(predecesores, 'A', 'F')
    print(f"\nCamino más corto de A a F: {' → '.join(camino_af)}")
    print(f"Distancia total: {distancias['F']}")