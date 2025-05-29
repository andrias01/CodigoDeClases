"""
PROBLEMA: Determinar si un número entero es un palíndromo sin convertirlo a string.
Un palíndromo lee igual de izquierda a derecha que de derecha a izquierda.

EJEMPLOS:
- 121 es palíndromo
- -121 no es palíndromo (se lee como 121-)
- 10 no es palíndromo (se lee como 01)

SOLUCIÓN: Invertir la mitad del número y comparar con la otra mitad.

COMPLEJIDAD: O(log n) tiempo, O(1) espacio

VISUALIZACIÓN: https://assets.leetcode.com/uploads/2019/01/04/palindrome.png
"""

def es_palindromo(x):
    """
    Determina si un número es palíndromo sin usar conversión a string.
    
    Args:
        x: Número entero
        
    Returns:
        True si es palíndromo, False en caso contrario
    """
    # Los números negativos no son palíndromos
    if x < 0:
        return False
    
    # Los números de un dígito son palíndromos
    if x < 10:
        return True
    
    # Los números que terminan en 0 (excepto 0) no son palíndromos
    if x % 10 == 0:
        return False
    
    # Invertir la mitad del número
    numero_invertido = 0
    while x > numero_invertido:
        numero_invertido = numero_invertido * 10 + x % 10
        x //= 10
    
    # Para números con cantidad par de dígitos: x == numero_invertido
    # Para números con cantidad impar de dígitos: x == numero_invertido // 10
    return x == numero_invertido or x == numero_invertido // 10

# Ejemplo de uso
if __name__ == "__main__":
    casos_prueba = [121, -121, 10, 12321, 1234321]
    for caso in casos_prueba:
        resultado = es_palindromo(caso)
        print(f"{caso} es palíndromo: {resultado}")