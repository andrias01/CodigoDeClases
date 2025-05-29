"""
Problema A: Un Problema Muy Fácil

DESCRIPCIÓN DEL PROBLEMA:
Este es un problema básico de programación que típicamente involucra operaciones
aritméticas simples o manipulación básica de datos. El objetivo es resolver
un problema fundamental que sirve como introducción a la programación competitiva.

PROBLEMA ESPECÍFICO:
Dados dos números enteros a y b, calcular su suma, resta, multiplicación y división.
También determinar cuál es el mayor y si son iguales.

SOLUCIÓN:
La solución implementa operaciones aritméticas básicas y comparaciones simples
usando estructuras condicionales básicas.

Visualización: https://pythontutor.com/visualize.html#mode=display
"""

def problema_facil(a, b):
    """
    Resuelve operaciones básicas entre dos números
    
    Args:
        a (int): Primer número
        b (int): Segundo número
    
    Returns:
        dict: Diccionario con todos los resultados
    """
    resultados = {}
    
    # Operaciones básicas
    resultados['suma'] = a + b
    resultados['resta'] = a - b
    resultados['multiplicacion'] = a * b
    
    # División con manejo de división por cero
    if b != 0:
        resultados['division'] = a / b
    else:
        resultados['division'] = "No se puede dividir por cero"
    
    # Comparaciones
    if a > b:
        resultados['mayor'] = f"{a} es mayor que {b}"
    elif b > a:
        resultados['mayor'] = f"{b} es mayor que {a}"
    else:
        resultados['mayor'] = f"{a} y {b} son iguales"
    
    return resultados

def main():
    """
    Función principal para ejecutar el problema
    """
    print("=== PROBLEMA A: UN PROBLEMA MUY FÁCIL ===")
    print("Ingrese dos números para realizar operaciones básicas")
    
    try:
        # Entrada de datos
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        
        # Procesar
        resultados = problema_facil(a, b)
        
        # Mostrar resultados
        print(f"\nResultados para {a} y {b}:")
        print(f"Suma: {resultados['suma']}")
        print(f"Resta: {resultados['resta']}")
        print(f"Multiplicación: {resultados['multiplicacion']}")
        print(f"División: {resultados['division']}")
        print(f"Comparación: {resultados['mayor']}")
        
    except ValueError:
        print("Error: Por favor ingrese números válidos")

if __name__ == "__main__":
    main()