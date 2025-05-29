"""
Búsqueda Binaria (Binary Search)

DESCRIPCIÓN DEL PROBLEMA:
La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una
lista ORDENADA. Funciona dividiendo repetitivamente la lista por la mitad y
comparando el elemento del medio con el valor buscado.

REQUISITOS:
- La lista DEBE estar ordenada (ascendente o descendentemente)

CARACTERÍSTICAS:
- Complejidad temporal: O(log n)
- Complejidad espacial: O(1) iterativa, O(log n) recursiva
- Mucho más eficiente que la búsqueda lineal para listas grandes

FUNCIONAMIENTO:
1. Definir límites: inicio = 0, fin = longitud - 1
2. Calcular el punto medio
3. Comparar el elemento del medio con el valor buscado
4. Si es igual: encontrado
5. Si es menor: buscar en la mitad derecha
6. Si es mayor: buscar en la mitad izquierda
7. Repetir hasta encontrar o hasta que inicio > fin

Visualización: https://visualgo.net/en/sorting (Binary Search)
"""

def busqueda_binaria_iterativa(lista, elemento_buscado):
    """
    Implementación iterativa de la búsqueda binaria
    
    Args:
        lista (list): Lista ordenada donde buscar
        elemento_buscado: Elemento que queremos encontrar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no se encuentra
    """
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        # Calcular el punto medio evitando overflow
        medio = inicio + (fin - inicio) // 2
        
        # Si encontramos el elemento
        if lista[medio] == elemento_buscado:
            return medio
        # Si el elemento del medio es menor, buscar en la mitad derecha
        elif lista[medio] < elemento_buscado:
            inicio = medio + 1
        # Si el elemento del medio es mayor, buscar en la mitad izquierda
        else:
            fin = medio - 1
    
    # Elemento no encontrado
    return -1

def busqueda_binaria_recursiva(lista, elemento_buscado, inicio=0, fin=None):
    """
    Implementación recursiva de la búsqueda binaria
    
    Args:
        lista (list): Lista ordenada donde buscar
        elemento_buscado: Elemento que queremos encontrar
        inicio (int): Índice de inicio de la búsqueda
        fin (int): Índice de fin de la búsqueda
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no se encuentra
    """
    # Si es la primera llamada, establecer fin
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: rango inválido
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = inicio + (fin - inicio) // 2
    
    # Si encontramos el elemento
    if lista[medio] == elemento_buscado:
        return medio
    # Si el elemento del medio es menor, buscar en la mitad derecha
    elif lista[medio] < elemento_buscado:
        return busqueda_binaria_recursiva(lista, elemento_buscado, medio + 1, fin)
    # Si el elemento del medio es mayor, buscar en la mitad izquierda
    else:
        return busqueda_binaria_recursiva(lista, elemento_buscado, inicio, medio - 1)

def busqueda_binaria_detallada(lista, elemento_buscado):
    """
    Búsqueda binaria con información detallada del proceso
    
    Args:
        lista (list): Lista ordenada donde buscar
        elemento_buscado: Elemento que queremos encontrar
    
    Returns:
        tuple: (índice, número_de_iteraciones)
    """
    print(f"Buscando {elemento_buscado} en la lista ordenada: {lista}")
    
    inicio = 0
    fin = len(lista) - 1
    iteraciones = 0
    
    while inicio <= fin:
        iteraciones += 1
        medio = inicio + (fin - inicio) // 2
        
        print(f"\nIteración {iteraciones}:")
        print(f"  Rango: [{inicio}, {fin}]")
        print(f"  Medio: índice {medio}, valor {lista[medio]}")
        print(f"  ¿{lista[medio]} == {elemento_buscado}?", end=" ")
        
        if lista[medio] == elemento_buscado:
            print("¡SÍ! ✅")
            print(f"  Elemento encontrado en la posición {medio}")
            return medio, iteraciones
        elif lista[medio] < elemento_buscado:
            print("No, es menor. Buscar en mitad derecha ➡️")
            inicio = medio + 1
        else:
            print("No, es mayor. Buscar en mitad izquierda ⬅️")
            fin = medio - 1
    
    print(f"\nElemento no encontrado después de {iteraciones} iteraciones")
    return -1, iteraciones

def verificar_ordenamiento(lista):
    """
    Verifica si una lista está ordenada
    
    Args:
        lista (list): Lista a verificar
    
    Returns:
        bool: True si está ordenada, False en caso contrario
    """
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

def main():
    """
    Función principal para demostrar la búsqueda binaria
    """
    print("=== ALGORITMO DE BÚSQUEDA BINARIA ===")
    
    # Ejemplos de prueba
    ejemplos = [
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 12),
        ([1, 2, 3, 4, 5], 6),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90], 30),
        ([], 5)
    ]
    
    for i, (lista, elemento) in enumerate(ejemplos, 1):
        print(f"\n{'='*50}")
        print(f"EJEMPLO {i}")
        print(f"{'='*50}")
        
        # Verificar que la lista esté ordenada
        if lista and not verificar_ordenamiento(lista):
            print("⚠️  ADVERTENCIA: La lista no está ordenada. Ordenando...")
            lista.sort()
        
        # Búsqueda iterativa
        resultado_iterativo = busqueda_binaria_iterativa(lista, elemento)
        print(f"Búsqueda iterativa: ", end="")
        if resultado_iterativo != -1:
            print(f"✅ Encontrado en posición {resultado_iterativo}")
        else:
            print("❌ No encontrado")
        
        # Búsqueda recursiva
        resultado_recursivo = busqueda_binaria_recursiva(lista, elemento)
        print(f"Búsqueda recursiva: ", end="")
        if resultado_recursivo != -1:
            print(f"✅ Encontrado en posición {resultado_recursivo}")
        else:
            print("❌ No encontrado")
        
        # Proceso detallado para los primeros 3 ejemplos
        if i <= 3:
            print(f"\nProceso detallado:")
            busqueda_binaria_detallada(lista, elemento)
    
    # Comparación de eficiencia
    print(f"\n{'='*50}")
    print("COMPARACIÓN DE EFICIENCIA")
    print(f"{'='*50}")
    
    import math
    tamaños = [10, 100, 1000, 10000]
    
    print("Comparación de iteraciones máximas:")
    print(f"{'Tamaño':<10} {'Búsqueda Lineal':<18} {'Búsqueda Binaria':<18}")
    print("-" * 50)
    
    for tamaño in tamaños:
        lineal = tamaño
        binaria = math.ceil(math.log2(tamaño))
        print(f"{tamaño:<10} {lineal:<18} {binaria:<18}")
    
    # Demostración interactiva
    print(f"\n{'='*50}")
    print("DEMOSTRACIÓN INTERACTIVA")
    print(f"{'='*50}")
    
    try:
        lista_usuario = input("Ingrese una lista de números separados por comas: ")
        lista = [int(x.strip()) for x in lista_usuario.split(',')]
        
        # Verificar y ordenar si es necesario
        if not verificar_ordenamiento(lista):
            print("Lista no ordenada. Ordenando automáticamente...")
            lista.sort()
            print(f"Lista ordenada: {lista}")
        
        elemento = int(input("Ingrese el número a buscar: "))
        
        print(f"\nBuscando {elemento} en {lista}...")
        indice, iteraciones = busqueda_binaria_detallada(lista, elemento)
        
        print(f"\nResumen:")
        print(f"Total de iteraciones: {iteraciones}")
        print(f"Máximo posible: {math.ceil(math.log2(len(lista))) if lista else 0}")
        
    except ValueError:
        print("Error: Por favor ingrese números válidos")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()