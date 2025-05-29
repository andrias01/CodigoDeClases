"""
Búsqueda Lineal (Linear Search)

DESCRIPCIÓN DEL PROBLEMA:
La búsqueda lineal es el algoritmo de búsqueda más simple. Consiste en recorrer
secuencialmente una lista o arreglo desde el primer elemento hasta encontrar
el elemento buscado o hasta llegar al final de la lista.

CARACTERÍSTICAS:
- Complejidad temporal: O(n) en el peor caso
- Complejidad espacial: O(1)
- Funciona en listas ordenadas y no ordenadas
- Es el más intuitivo pero no el más eficiente para listas grandes

FUNCIONAMIENTO:
1. Comenzar desde el primer elemento de la lista
2. Comparar cada elemento con el valor buscado
3. Si se encuentra el elemento, devolver su posición
4. Si se recorre toda la lista sin encontrarlo, devolver -1

Visualización: https://visualgo.net/en/sorting (Linear Search)
"""

def busqueda_lineal(lista, elemento_buscado):
    """
    Implementa el algoritmo de búsqueda lineal
    
    Args:
        lista (list): Lista donde buscar el elemento
        elemento_buscado: Elemento que queremos encontrar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no se encuentra
    """
    # Recorrer cada elemento de la lista con su índice
    for indice, elemento in enumerate(lista):
        # Si encontramos el elemento buscado
        if elemento == elemento_buscado:
            return indice
    
    # Si llegamos aquí, el elemento no está en la lista
    return -1

def busqueda_lineal_detallada(lista, elemento_buscado):
    """
    Implementación de búsqueda lineal con información detallada del proceso
    
    Args:
        lista (list): Lista donde buscar el elemento
        elemento_buscado: Elemento que queremos encontrar
    
    Returns:
        tuple: (índice, número_de_comparaciones)
    """
    print(f"Buscando {elemento_buscado} en la lista: {lista}")
    comparaciones = 0
    
    for indice, elemento in enumerate(lista):
        comparaciones += 1
        print(f"Comparación {comparaciones}: ¿{elemento} == {elemento_buscado}?", end=" ")
        
        if elemento == elemento_buscado:
            print("¡SÍ! ✅")
            print(f"Elemento encontrado en la posición {indice}")
            return indice, comparaciones
        else:
            print("No ❌")
    
    print(f"Elemento no encontrado después de {comparaciones} comparaciones")
    return -1, comparaciones

def busqueda_lineal_todos(lista, elemento_buscado):
    """
    Encuentra todas las ocurrencias de un elemento en la lista
    
    Args:
        lista (list): Lista donde buscar el elemento
        elemento_buscado: Elemento que queremos encontrar
    
    Returns:
        list: Lista con todos los índices donde se encuentra el elemento
    """
    indices_encontrados = []
    
    for indice, elemento in enumerate(lista):
        if elemento == elemento_buscado:
            indices_encontrados.append(indice)
    
    return indices_encontrados

def main():
    """
    Función principal para demostrar la búsqueda lineal
    """
    print("=== ALGORITMO DE BÚSQUEDA LINEAL ===")
    
    # Ejemplos de prueba
    ejemplos = [
        ([1, 3, 5, 7, 9, 11, 13], 7),
        ([10, 20, 30, 40, 50], 25),
        (['manzana', 'banana', 'cereza', 'durazno'], 'banana'),
        ([1, 2, 3, 2, 4, 2, 5], 2),
        ([], 5)
    ]
    
    for i, (lista, elemento) in enumerate(ejemplos, 1):
        print(f"\n--- EJEMPLO {i} ---")
        
        # Búsqueda simple
        resultado = busqueda_lineal(lista, elemento)
        if resultado != -1:
            print(f"✅ Elemento '{elemento}' encontrado en la posición {resultado}")
        else:
            print(f"❌ Elemento '{elemento}' no encontrado")
        
        # Búsqueda detallada (solo para los primeros 3 ejemplos)
        if i <= 3:
            print("\nProceso detallado:")
            busqueda_lineal_detallada(lista, elemento)
        
        # Buscar todas las ocurrencias para el ejemplo 4
        if i == 4:
            todas_ocurrencias = busqueda_lineal_todos(lista, elemento)
            print(f"Todas las posiciones donde aparece '{elemento}': {todas_ocurrencias}")
    
    # Demostración interactiva
    print("\n=== DEMOSTRACIÓN INTERACTIVA ===")
    try:
        lista_usuario = input("Ingrese una lista de números separados por comas: ")
        lista = [int(x.strip()) for x in lista_usuario.split(',')]
        elemento = int(input("Ingrese el número a buscar: "))
        
        print(f"\nBuscando {elemento} en {lista}...")
        indice, comparaciones = busqueda_lineal_detallada(lista, elemento)
        
        print(f"\nResumen:")
        print(f"Total de comparaciones: {comparaciones}")
        print(f"Eficiencia: {comparaciones}/{len(lista)} elementos revisados")
        
    except ValueError:
        print("Error: Por favor ingrese números válidos")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()