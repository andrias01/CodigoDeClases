import time
#_________________________________________
#_________________________________________
#_________________________________________
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
#_________________________________________
import time
import random
import matplotlib.pyplot as plt

# Parámetros generales
N = 8 # Tamaño del tablero y número de reinas
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
    poblacion = [crear_individuo() for _ in range(POBLACION_INICIAL)]#400
    for generacion in range(GENERACIONES):#500
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
# Visualización del tablero de ajedrez
def mostrar_tablero_grafico(solucion):
    tamaño = N
    fig, ax = plt.subplots()

    # Dibujar casillas del tablero
    for fila in range(tamaño):
        for col in range(tamaño):
            color = 'cornsilk' if (fila + col) % 2 == 0 else 'gray'
            ax.add_patch(plt.Rectangle((col, tamaño - fila - 1), 1, 1, color=color))

    # Dibujar reinas (ajustando fila - 1)
    for col, fila in enumerate(solucion):
        fila_ajustada = fila
        ax.text(col + 0.5, tamaño - fila_ajustada - 0.5, '♛',
                ha='center', va='center', fontsize=30, color='red')

    ax.set_xlim(0, tamaño)
    ax.set_ylim(0, tamaño)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Solución de las 8 Reinas", fontsize=16)
    plt.show()
    
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

mostrar_tablero_grafico(solucion)


# Exportar la solución a un archivo CSV
with open("solucion_8_reinas.csv", "w") as f:
    f.write(",".join(map(str, solucion)))
print("\nSolución exportada a 'solucion_8_reinas.csv'")
time.sleep(200)
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

# ' Código VBA para visualizar el tablero de ajedrez en Excel
# ' Este código debe ser ejecutado en el entorno de Excel VBA
# con las teclas alt + F11
# ' y luego pegado en un módulo nuevo.
# ' Procedimiento principal para visualizar el tablero de ajedrez
# Sub MostrarTablero8Reinas()
#     ' Definir variables
#     Dim solucion() As Integer
#     Dim tablero As Range
#     Dim fila As Integer, columna As Integer
    
#     ' Obtener la solución del algoritmo genético en Python
#     ' Aquí puedes usar diferentes métodos:
#     ' 1. Leer datos desde un archivo CSV exportado por Python
#     ' 2. Ingresar la solución manualmente
#     ' Para este ejemplo, usaremos la solución que has encontrado con tu código Python
    
#     ' Asumamos que guardaste tu solución en un archivo o la introduces manualmente
#     solucion = ObtenerSolucion()
    
#     ' Configurar hoja de Excel
#     Application.ScreenUpdating = False
#     Sheets.Add.Name = "Tablero8Reinas"
#     Set tablero = Sheets("Tablero8Reinas").Range("B2:I9")
    
#     ' Configurar el formato del tablero
#     ConfigurarTablero tablero
    
#     ' Colocar las reinas en el tablero
#     For columna = 0 To 7
#         fila = solucion(columna)
#         ColocarReina tablero, fila, columna
#     Next columna
    
#     ' Ajustar tamaño de celdas y centrar la vista
#     tablero.EntireColumn.ColumnWidth = 8
#     tablero.EntireRow.RowHeight = 50
#     tablero.Select
    
#     Application.ScreenUpdating = True
    
#     MsgBox "Tablero de 8 reinas creado exitosamente.", vbInformation
# End Sub

# ' Función para obtener la solución del algoritmo genético
# Function ObtenerSolucion() As Integer()
#     Dim solucion(7) As Integer
    
#     ' Opción 1: Leer desde un archivo CSV generado por Python
#     ' Uncomment and adjust the code below if using CSV
#     '
#     ' Dim fso As Object, txtFile As Object, filePath As String
#     ' Dim txtLine As String
#     ' Set fso = CreateObject("Scripting.FileSystemObject")
#     ' filePath = Application.GetOpenFilename("Archivos CSV (*.csv),*.csv", , "Selecciona el archivo con la solución")
#     ' If filePath <> "False" Then
#     '     Set txtFile = fso.OpenTextFile(filePath, 1)
#     '     txtLine = txtFile.ReadLine
#     '     txtFile.Close
#     '     
#     '     Dim valores As Variant
#     '     valores = Split(txtLine, ",")
#     '     For i = 0 To 7
#     '         solucion(i) = CInt(valores(i))
#     '     Next i
#     ' End If
    
#     ' Opción 2: Introducir manualmente la solución que obtuviste con Python
#     ' Reemplaza estos valores con la solución generada por tu algoritmo genético
#     solucion(0) = 0
#     solucion(1) = 4
#     solucion(2) = 7
#     solucion(3) = 5
#     solucion(4) = 2
#     solucion(5) = 6
#     solucion(6) = 1
#     solucion(7) = 3
    
#     ' También podría ser a través de un InputBox para cada posición
#     ' For i = 0 To 7
#     '     solucion(i) = CInt(InputBox("Ingresa la fila para la reina en la columna " & i & " (0-7):"))
#     ' Next i
    
#     ObtenerSolucion = solucion
# End Function

# ' Procedimiento para configurar el aspecto visual del tablero
# Sub ConfigurarTablero(tablero As Range)
#     Dim fila As Integer, columna As Integer
#     Dim celda As Range
    
#     ' Colorear el tablero en patrón de ajedrez
#     For fila = 1 To 8
#         For columna = 1 To 8
#             Set celda = tablero.Cells(fila, columna)
            
#             ' Configurar celda
#             With celda
#                 .HorizontalAlignment = xlCenter
#                 .VerticalAlignment = xlCenter
#                 .Font.Size = 20
#                 .Font.Bold = True
                
#                 ' Patrón de colores del tablero
#                 If (fila + columna) Mod 2 = 0 Then
#                     .Interior.Color = RGB(255, 206, 158) ' Color claro
#                 Else
#                     .Interior.Color = RGB(209, 139, 71) ' Color oscuro
#                 End If
                
#                 .Borders.LineStyle = xlContinuous
#                 .Borders.Weight = xlThin
#             End With
#         Next columna
#     Next fila
    
#     ' Añadir coordenadas alrededor del tablero
#     For i = 1 To 8
#         ' Números de fila (1-8)
#         Sheets("Tablero8Reinas").Cells(i + 1, 1).Value = 9 - i
#         Sheets("Tablero8Reinas").Cells(i + 1, 1).Font.Bold = True
#         Sheets("Tablero8Reinas").Cells(i + 1, 1).HorizontalAlignment = xlCenter
        
#         ' Letras de columna (a-h)
#         Sheets("Tablero8Reinas").Cells(1, i + 1).Value = Chr(96 + i)
#         Sheets("Tablero8Reinas").Cells(1, i + 1).Font.Bold = True
#         Sheets("Tablero8Reinas").Cells(1, i + 1).HorizontalAlignment = xlCenter
#     Next i
# End Sub

# ' Procedimiento para colocar una reina en el tablero
# Sub ColocarReina(tablero As Range, fila As Integer, columna As Integer)
#     ' Coloca el símbolo de la reina (♛) en la celda correspondiente
#     tablero.Cells(fila + 1, columna + 1).Value = "♛"
#     ' También podrías usar "R" o ChrW(9819) que es el código Unicode para la reina
# End Sub

# ' Procedimiento alternativo para exportar la solución desde Python
# Sub ImportarSolucionDesdeArchivo()
#     Dim filePath As String
#     filePath = Application.GetOpenFilename("Archivos CSV (*.csv),*.csv", , "Selecciona el archivo con la solución")
    
#     If filePath <> "False" Then
#         With Sheets.Add.Name = "DatosSolucion"
#             .Range("A1").Select
#             With ActiveSheet.QueryTables.Add(Connection:="TEXT;" & filePath, Destination:=Range("A1"))
#                 .Name = "Solución"
#                 .FieldNames = True
#                 .RowNumbers = False
#                 .FillAdjacentFormulas = False
#                 .PreserveFormatting = True
#                 .RefreshOnFileOpen = False
#                 .RefreshStyle = xlInsertDeleteCells
#                 .SavePassword = False
#                 .SaveData = True
#                 .RefreshPeriod = 0
#                 .TextFilePromptOnRefresh = False
#                 .TextFilePlatform = 437
#                 .TextFileStartRow = 1
#                 .TextFileParseType = xlDelimited
#                 .TextFileTextQualifier = xlTextQualifierDoubleQuote
#                 .TextFileConsecutiveDelimiter = False
#                 .TextFileTabDelimiter = False
#                 .TextFileSemicolonDelimiter = False
#                 .TextFileCommaDelimiter = True
#                 .TextFileSpaceDelimiter = False
#                 .TextFileColumnDataTypes = Array(1, 1, 1, 1, 1, 1, 1, 1)
#                 .Refresh BackgroundQuery:=False
#             End With
            
#             ' Luego puedes leer los valores de la solución desde esta hoja
#             ' y usarlos para el procedimiento MostrarTablero8Reinas
#         End With
#     End If
# End Sub

#_________________________________________
# import matplotlib.pyplot as plt
# Importamos NumPy para manejo de arreglos
import numpy as np
# Importamos el módulo de algoritmo genético
from geneticalgorithm import geneticalgorithm as ga

# --------------------------------------
# Parámetros generales del problema
# --------------------------------------

# Tamaño del tablero (8x8)
tamaño_tablero = 8

# Número de variables del problema (una por columna)
dimension = tamaño_tablero

# Máximo valor posible de "fitness" (es decir, 0 ataques entre reinas)
# Se calcula cuántos pares únicos de reinas se pueden formar: C(n,2)
maximo_fitness = (tamaño_tablero * (tamaño_tablero - 1)) / 2


# def mostrar_tablero_grafico(solucion):
#     tamaño = len(solucion)
#     fig, ax = plt.subplots()
#     # Dibujar las casillas
#     for fila in range(tamaño):
#         for col in range(tamaño):
#             color = 'cornsilk' if (fila + col) % 2 == 0 else 'gray'
#             ax.add_patch(plt.Rectangle((col, tamaño - fila - 1), 1, 1, color=color))
    
#     # Dibujar las reinas
#     for col, fila in enumerate(solucion):
#         ax.text(col + 0.5, tamaño - fila + 0.5 - 1, '♛', ha='center', va='center', fontsize=30, color='red')
    
#     ax.set_xlim(0, tamaño)
#     ax.set_ylim(0, tamaño)
#     ax.set_xticks([])
#     ax.set_yticks([])
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.title("Solución de las 8 Reinas", fontsize=16)
#     plt.show()

# --------------------------------------
# Función para verificar cuántos ataques hay en el tablero
# --------------------------------------

def verificar_ataques(estado_tablero):
    ataques = 0
    # Comparamos cada reina con las demás que están a su derecha
    for i in range(tamaño_tablero):
        for j in range(i + 1, tamaño_tablero):
            # Si están en la misma fila o en la misma diagonal, hay un ataque
            if estado_tablero[i] == estado_tablero[j] or abs(estado_tablero[i] - estado_tablero[j]) == j - i:
                ataques += 1
    return ataques

# --------------------------------------
# Función objetivo del algoritmo genético (a minimizar)
# --------------------------------------

def calcular_fitness(X):
    cromosoma = X.astype(int).tolist()
    ataques = verificar_ataques(cromosoma)
    # El fitness ideal es 0 ataques, así que se devuelve el negativo para que el algoritmo lo minimice
    return -(maximo_fitness - ataques)

# --------------------------------------
# Definición del espacio de búsqueda
# Cada variable (reina) puede ir en una fila entre 1 y 8
# (una reina por columna)
# --------------------------------------

limites_variables = np.array([[1, tamaño_tablero]] * dimension)

# --------------------------------------
# Configuración del algoritmo genético
# --------------------------------------

parametros_algoritmo = {
    'max_num_iteration': 1000,        # Número máximo de generaciones
    'population_size': 100,          # Tamaño de la población
    'mutation_probability': 0.1,     # Probabilidad de mutación
    'elit_ratio': 0.01,              # Porcentaje de élite que pasa directamente a la siguiente generación
    'crossover_probability': 0.5,    # Probabilidad de cruce
    'parents_portion': 0.3,          # Porcentaje de padres seleccionados
    'crossover_type': 'uniform',     # Tipo de cruce (uniforme en este caso)
    'max_iteration_without_improv': None  # Iteraciones sin mejora antes de detenerse
}

# --------------------------------------
# Inicialización del modelo genético
# --------------------------------------

modelo = ga(
    function=calcular_fitness,               # Función objetivo a minimizar
    dimension=dimension,                     # Número de variables
    variable_type='int',                     # Tipo de variable: entero
    variable_boundaries=limites_variables,   # Límites por variable
    algorithm_parameters=parametros_algoritmo
)

# --------------------------------------
# Ejecutamos el algoritmo
# --------------------------------------
def imprimir_tablero(solucion):
    for fila in range(len(solucion)):
        linea = ""
        for columna in range(len(solucion)):
            if solucion[columna] == fila + 1:  # fila +1 porque el resultado va de 1 a 8
                linea += " Q "
            else:
                linea += " . "
        print(linea)

# mostrar_tablero_grafico(mejor_solucion)
modelo.run()
# Obtener la mejor solución encontrada
mejor_solucion = modelo.output_dict['variable'].astype(int).tolist()

print("\nTablero solución (modo texto):")
imprimir_tablero(mejor_solucion)


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