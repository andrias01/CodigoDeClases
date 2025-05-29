"""
PROBLEMA: Calcular el factorial de un número n (n!).
El factorial se define como: n! = n × (n-1) × (n-2) × ... × 2 × 1
Por convención: 0! = 1

EJEMPLOS:
5! = 5 × 4 × 3 × 2 × 1 = 120
3! = 3 × 2 × 1 = 6
0! = 1

SOLUCIONES:
1. Recursiva: Elegante y natural
2. Iterativa: Más eficiente en espacio

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/f/f3/Factorial_Recursion.png
"""

def factorial_recursivo(n):
    """
    Calcula el factorial usando recursión.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        El factorial de n
        
    Complejidad: O(n) tiempo, O(n) espacio (stack)
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Llamada recursiva
    return n * factorial_recursivo(n - 1)


def factorial_iterativo(n):
    """
    Calcula el factorial usando iteración.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        El factorial de n
        
    Complejidad: O(n) tiempo, O(1) espacio
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    numeros_prueba = [0, 1, 5, 10]
    
    for num in numeros_prueba:
        print(f"{num}! = {factorial_iterativo(num)} (iterativo)")
        print(f"{num}! = {factorial_recursivo(num)} (recursivo)")
        print()