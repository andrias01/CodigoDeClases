import time
import random
import matplotlib.pyplot as plt

def dijkstra(grafo, inicio, fin=None):
    """
    Implementación del algoritmo de Dijkstra para encontrar el camino más corto
    desde un nodo de origen a todos los demás nodos.
    
    Args:
        grafo: Matriz de adyacencia donde grafo[i][j] representa el peso de la arista del nodo i al nodo j
               (un valor de 0 indica que no hay conexión)
        inicio: Nodo de origen
        fin: Nodo destino (opcional, si solo queremos el camino a un nodo específico)
    
    Returns:
        distancias: Lista donde cada elemento contiene [distancia acumulada, nodo de procedencia]
    """
    num_nodos = len(grafo)
    
    # Inicializar distancias: [distancia acumulada, nodo de procedencia]
    # Usamos math.inf para representar infinito
    import math
    distancias = [[math.inf, '-'] for _ in range(num_nodos)]
    distancias[inicio] = [0, '-']  # Distancia al nodo inicial es 0
    
    # Conjunto de nodos visitados
    visitados = [False] * num_nodos
    
    for _ in range(num_nodos):
        # Encontrar el nodo no visitado con la distancia mínima
        distancia_min = math.inf
        nodo_min = -1
        
        for i in range(num_nodos):
            if not visitados[i] and distancias[i][0] < distancia_min:
                distancia_min = distancias[i][0]
                nodo_min = i
        
        # Si no encontramos ningún nodo accesible, terminamos
        if nodo_min == -1:
            break
            
        # Marcar el nodo como visitado
        visitados[nodo_min] = True
        
        # Si hemos llegado al nodo destino, podemos terminar
        if fin is not None and nodo_min == fin:
            break
        
        # Actualizar las distancias de los nodos adyacentes
        for i in range(num_nodos):
            # Si hay una arista desde nodo_min hasta i
            if grafo[nodo_min][i] > 0:
                # Calcular nueva distancia potencial
                nueva_distancia = distancias[nodo_min][0] + grafo[nodo_min][i]
                
                # Si la nueva distancia es menor que la actual
                if nueva_distancia < distancias[i][0]:
                    # Actualizar distancia y nodo de procedencia
                    # Convertimos nodo_min a letra (A=0, B=1, etc.)
                    nodo_origen = chr(nodo_min + 65)  # 65 es el código ASCII de 'A'
                    distancias[i] = [nueva_distancia, nodo_origen]
    
    return distancias

def imprimir_camino(distancias, inicio, fin):
    """
    Imprime el camino más corto desde el nodo de inicio al nodo final.
    
    Args:
        distancias: Resultado del algoritmo de Dijkstra
        inicio: Nodo de origen
        fin: Nodo destino
    
    Returns:
        Una lista con los nodos del camino
    """
    import math
    
    if distancias[fin][0] == math.inf:
        print(f"No hay camino de {chr(inicio + 65)} a {chr(fin + 65)}")
        return []
    
    camino = []
    actual = fin
    
    # Reconstruir el camino desde el final hasta el inicio
    while actual != inicio:
        camino.append(chr(actual + 65))
        # Encontrar el nodo de procedencia
        nodo_origen = ord(distancias[actual][1]) - 65
        actual = nodo_origen
    
    camino.append(chr(inicio + 65))
    camino.reverse()
    
    print(f"Camino más corto de {chr(inicio + 65)} a {chr(fin + 65)}: {' -> '.join(camino)}")
    print(f"Distancia total: {distancias[fin][0]}")
    
    # Convertir el camino de letras a índices
    camino_indices = [ord(nodo) - 65 for nodo in camino]
    return camino_indices

def crear_grafo_manual(num_nodos, aristas=None):
    """
    Crea un grafo manualmente especificando las aristas y sus pesos.
    
    Args:
        num_nodos: Número de nodos en el grafo
        aristas: Lista de tuplas (origen, destino, peso) donde origen y destino son 
                índices (0 para A, 1 para B, etc.) o letras ('A', 'B', etc.)
    
    Returns:
        Matriz de adyacencia que representa el grafo
    """
    grafo = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)]
    
    if aristas:
        for arista in aristas:
            # Si el origen y destino se proporcionan como letras, convertirlos a índices
            if isinstance(arista[0], str):
                origen = ord(arista[0].upper()) - 65  # 'A' -> 0, 'B' -> 1, etc.
            else:
                origen = arista[0]
                
            if isinstance(arista[1], str):
                destino = ord(arista[1].upper()) - 65
            else:
                destino = arista[1]
                
            peso = arista[2]
            
            # Verificar que los índices son válidos
            if 0 <= origen < num_nodos and 0 <= destino < num_nodos:
                grafo[origen][destino] = peso
    
    return grafo

def visualizar_grafo(grafo, camino=None):
    """
    Visualiza el grafo y el camino más corto usando matplotlib.
    
    Args:
        grafo: Matriz de adyacencia del grafo
        camino: Lista de índices de nodos que forman el camino más corto (opcional)
    """
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np
    
    # Crear un grafo dirigido
    G = nx.DiGraph()
    
    # Número de nodos
    num_nodos = len(grafo)
    
    # Añadir nodos con etiquetas de letras
    node_labels = {}
    for i in range(num_nodos):
        letra = chr(i + 65)  # Convertir índice a letra (A, B, C...)
        G.add_node(letra)
        node_labels[letra] = letra
    
    # Añadir aristas con pesos
    for i in range(num_nodos):
        for j in range(num_nodos):
            if grafo[i][j] > 0:
                origen = chr(i + 65)
                destino = chr(j + 65)
                G.add_edge(origen, destino, weight=grafo[i][j])
    
    # Crear figura
    plt.figure(figsize=(12, 8))
    
    # Posicionamiento de los nodos en círculo
    pos = nx.circular_layout(G)
    
    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    
    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=14, font_weight='bold')
    
    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, arrowsize=15)
    
    # Dibujar pesos de aristas
    edge_labels = {}
    for i in range(num_nodos):
        for j in range(num_nodos):
            if grafo[i][j] > 0:
                origen = chr(i + 65)
                destino = chr(j + 65)
                edge_labels[(origen, destino)] = grafo[i][j]
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_weight='bold')
    
    # Si se proporciona un camino, resaltar las aristas
    if camino and len(camino) > 1:
        # Convertir los índices del camino a letras
        camino_letras = [chr(idx + 65) for idx in camino]
        
        # Crear pares de nodos para las aristas del camino
        camino_aristas = [(camino_letras[i], camino_letras[i + 1]) for i in range(len(camino_letras) - 1)]
        
        # Resaltar las aristas del camino
        nx.draw_networkx_edges(G, pos, edgelist=camino_aristas, width=3.0, edge_color='red', arrowsize=20)
    
    plt.title("Visualización del Grafo y Camino Más Corto", size=15)
    plt.axis('off')
    
    # Mostrar la visualización
    plt.tight_layout()
    plt.savefig('grafo_visualizado.png')
    plt.close()

# Definir un único grafo para analizar
num_nodos = 8  # Grafo con 8 nodos (A-H)

# Definir las aristas del grafo
# Formato: (origen, destino, peso)
aristas = [
    ('A', 'B', 3),  # A -> B con peso 3
    ('A', 'C', 1),  # A -> C con peso 1
    ('B', 'D', 1),  # B -> D con peso 1
    ('B', 'G', 5),  # B -> G con peso 5
    ('C', 'D', 2),  # C -> D con peso 2
    ('C', 'F', 5),  # C -> F con peso 5
    ('D', 'E', 4),  # D -> E con peso 4
    ('D', 'F', 2),  # D -> F con peso 2
    ('E', 'G', 2),  # E -> G con peso 2
    ('E', 'H', 1),  # E -> H con peso 1
    ('F', 'H', 3),  # F -> H con peso 3
]

# Crear el grafo
grafo = crear_grafo_manual(num_nodos, aristas)

# Mostrar el grafo
print("Matriz de adyacencia del grafo:")
for i, fila in enumerate(grafo):
    print(f"{chr(65+i)}: {fila}")

# Nodo de origen para el algoritmo de Dijkstra
nodo_inicio = 0  # 0 = A
nodo_destino = 7  # 7 = H

# Ejecutar algoritmo de Dijkstra
resultado = dijkstra(grafo, nodo_inicio)

# Mostrar resultados
print("\nResultados del algoritmo de Dijkstra desde el nodo A:")
print("Nodo | [Distancia acumulada, Procedencia]")
print("-" * 40)

for i in range(num_nodos):
    nombre_nodo = chr(i + 65)
    distancia = resultado[i][0]
    import math
    if distancia == math.inf:
        texto_distancia = "inf"
    else:
        texto_distancia = str(distancia)
    
    nodo_origen = resultado[i][1]
    print(f"  {nombre_nodo}  | [{texto_distancia}, {nodo_origen}]")

# Visualizar el grafo completo
visualizar_grafo(grafo)
print("\nSe ha guardado la visualización del grafo como 'grafo_visualizado.png'")

# Encontrar el camino más corto al nodo destino
print(f"\nCamino más corto desde el nodo A hasta el nodo H:")
camino = imprimir_camino(resultado, nodo_inicio, nodo_destino)

# Visualizar el grafo con el camino resaltado
if camino:
    visualizar_grafo(grafo, camino)
    print("Se ha guardado la visualización del camino como 'grafo_visualizado.png' (sobrescribiendo el anterior)")

"""
# Para modificar el grafo, cambia la lista de aristas:
aristas = [
    ('A', 'B', 5),  # A -> B con peso 5
    ('B', 'C', 3),  # ... etc
    # Añade todas las conexiones que necesites
]

# Y vuelve a crear el grafo:
grafo = crear_grafo_manual(num_nodos, aristas)

# Para cambiar los nodos de origen y destino, modifica:
nodo_inicio = 0  # 0 = A
nodo_destino = 7  # 7 = H
"""

# Quitar la espera al final
time.sleep(200)  # Comentado para que el programa termine inmediatamente