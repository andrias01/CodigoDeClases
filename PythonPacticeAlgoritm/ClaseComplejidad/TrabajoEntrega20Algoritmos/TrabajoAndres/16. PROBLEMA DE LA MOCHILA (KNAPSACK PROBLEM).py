"""
PROBLEMA: Dado un conjunto de objetos, cada uno con un peso y un valor, determinar
cuáles incluir en una mochila de capacidad limitada para maximizar el valor total.

VARIANTES:
1. 0/1 Knapsack: Cada objeto se puede tomar o no (implementado aquí)
2. Unbounded Knapsack: Se puede tomar cualquier cantidad de cada objeto
3. Bounded Knapsack: Cantidad limitada de cada objeto

TÉCNICA: Programación dinámica

COMPLEJIDAD: O(n*W) tiempo y espacio, donde n es el número de objetos y W la capacidad

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/f/fd/Knapsack.svg
"""

def mochila_01_dp(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica.
    
    Args:
        pesos: Lista de pesos de los objetos
        valores: Lista de valores de los objetos
        capacidad: Capacidad máxima de la mochila
        
    Returns:
        (valor_maximo, objetos_seleccionados)
    """
    n = len(pesos)
    
    # Crear tabla DP: dp[i][w] = máximo valor usando los primeros i objetos con capacidad w
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla DP
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            # Peso del objeto actual (índice i-1 porque dp tiene una fila extra)
            peso_actual = pesos[i - 1]
            valor_actual = valores[i - 1]
            
            if peso_actual <= w:
                # Podemos incluir el objeto: max(incluir, no incluir)
                incluir = valor_actual + dp[i - 1][w - peso_actual]
                no_incluir = dp[i - 1][w]
                dp[i][w] = max(incluir, no_incluir)
            else:
                # No podemos incluir el objeto
                dp[i][w] = dp[i - 1][w]
    
    # Rastrear qué objetos fueron seleccionados
    objetos_seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            objetos_seleccionados.append(i - 1)  # Índice del objeto
            w -= pesos[i - 1]
    
    objetos_seleccionados.reverse()
    valor_maximo = dp[n][capacidad]
    
    return valor_maximo, objetos_seleccionados


def mochila_01_optimizada(pesos, valores, capacidad):
    """
    Versión optimizada en espacio del problema de la mochila 0/1.
    Solo necesita O(W) espacio en lugar de O(n*W).
    
    Args:
        pesos: Lista de pesos de los objetos
        valores: Lista de valores de los objetos
        capacidad: Capacidad máxima de la mochila
        
    Returns:
        Valor máximo posible
    """
    n = len(pesos)
    dp = [0] * (capacidad + 1)
    
    for i in range(n):
        # Recorrer de derecha a izquierda para evitar usar valores ya actualizados
        for w in range(capacidad, pesos[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - pesos[i]] + valores[i])
    
    return dp[capacidad]


def mochila_recursiva_memo(pesos, valores, capacidad, n=None, memo=None):
    """
    Solución recursiva con memoización para el problema de la mochila.
    
    Args:
        pesos: Lista de pesos de los objetos
        valores: Lista de valores de los objetos
        capacidad: Capacidad actual disponible
        n: Número de objetos a considerar
        memo: Diccionario para memoización
        
    Returns:
        Valor máximo posible
    """
    if n is None:
        n = len(pesos)
    if memo is None:
        memo = {}
    
    # Caso base
    if n == 0 or capacidad == 0:
        return 0
    
    # Verificar si ya calculamos este subproblema
    if (n, capacidad) in memo:
        return memo[(n, capacidad)]
    
    # Si el peso del objeto actual es mayor que la capacidad, no se puede incluir
    if pesos[n - 1] > capacidad:
        resultado = mochila_recursiva_memo(pesos, valores, capacidad, n - 1, memo)
    else:
        # Máximo entre incluir y no incluir el objeto actual
        incluir = valores[n - 1] + mochila_recursiva_memo(pesos, valores, 
                                                          capacidad - pesos[n - 1], n - 1, memo)
        no_incluir = mochila_recursiva_memo(pesos, valores, capacidad, n - 1, memo)
        resultado = max(incluir, no_incluir)
    
    memo[(n, capacidad)] = resultado
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo: objetos con (peso, valor)
    objetos = [
        (2, 3),   # Objeto 0: peso=2, valor=3
        (3, 4),   # Objeto 1: peso=3, valor=4
        (4, 5),   # Objeto 2: peso=4, valor=5
        (5, 6),   # Objeto 3: peso=5, valor=6
        (1, 2)    # Objeto 4: peso=1, valor=2
    ]
    
    pesos = [obj[0] for obj in objetos]
    valores = [obj[1] for obj in objetos]
    capacidad_mochila = 8
    
    print("Problema de la Mochila")
    print("Objetos disponibles:")
    for i, (peso, valor) in enumerate(objetos):
        print(f"  Objeto {i}: peso={peso}, valor={valor}, relación={valor/peso:.2f}")
    print(f"Capacidad de la mochila: {capacidad_mochila}")
    print()
    
    # Resolver usando programación dinámica
    valor_max, objetos_sel = mochila_01_dp(pesos, valores, capacidad_mochila)
    peso_total = sum(pesos[i] for i in objetos_sel)
    
    print("Solución óptima (Programación Dinámica):")
    print(f"Valor máximo: {valor_max}")
    print(f"Objetos seleccionados: {objetos_sel}")
    print(f"Peso total: {peso_total}/{capacidad_mochila}")
    
    # Verificar con otros métodos
    valor_optimizado = mochila_01_optimizada(pesos, valores, capacidad_mochila)
    valor_recursivo = mochila_recursiva_memo(pesos, valores, capacidad_mochila)
    
    print(f"\nVerificación:")
    print(f"Método optimizado: {valor_optimizado}")
    print(f"Método recursivo: {valor_recursivo}")