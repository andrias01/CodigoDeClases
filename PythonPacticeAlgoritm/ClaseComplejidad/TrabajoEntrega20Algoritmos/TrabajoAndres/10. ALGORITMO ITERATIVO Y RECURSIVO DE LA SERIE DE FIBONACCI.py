"""
PROBLEMA: Calcular el n-ésimo número de la serie de Fibonacci.
La serie de Fibonacci se define como: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)

SERIE: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

SOLUCIONES:
1. Recursiva: Elegante pero ineficiente O(2^n)
2. Iterativa: Eficiente O(n) tiempo, O(1) espacio
3. Recursiva con memoización: O(n) tiempo y espacio

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/2/2e/FibonacciSpiral.svg
"""

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci usando recursión simple.
    
    Args:
        n: Posición en la serie (n >= 0)
        
    Returns:
        El n-ésimo número de Fibonacci
        
    Complejidad: O(2^n) tiempo, O(n) espacio (stack)
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    
    # Casos base
    if n <= 1:
        return n
    
    # Llamada recursiva
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci usando iteración.
    
    Args:
        n: Posición en la serie (n >= 0)
        
    Returns:
        El n-ésimo número de Fibonacci
        
    Complejidad: O(n) tiempo, O(1) espacio
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    
    if n <= 1:
        return n
    
    # Variables para almacenar los dos números anteriores
    anterior = 0  # F(0)
    actual = 1    # F(1)
    
    # Calcular desde F(2) hasta F(n)
    for i in range(2, n + 1):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
    
    return actual


def fibonacci_memoizado(n, memo=None):
    """
    Calcula el n-ésimo número de Fibonacci usando recursión con memoización.
    
    Args:
        n: Posición en la serie (n >= 0)
        memo: Diccionario para almacenar resultados calculados
        
    Returns:
        El n-ésimo número de Fibonacci
        
    Complejidad: O(n) tiempo, O(n) espacio
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("n debe ser no negativo")
    
    # Si ya calculamos este valor, lo retornamos
    if n in memo:
        return memo[n]
    
    # Casos base
    if n <= 1:
        return n
    
    # Calcular y guardar en memo
    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)
    return memo[n]

# Ejemplo de uso
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci de {n}:")
    print(f"Recursivo: {fibonacci_recursivo(n)}")
    print(f"Iterativo: {fibonacci_iterativo(n)}")
    print(f"Memoizado: {fibonacci_memoizado(n)}")
    
    # Mostrar la serie completa
    print(f"\nSerie de Fibonacci hasta {n}:")
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci_iterativo(i)}")