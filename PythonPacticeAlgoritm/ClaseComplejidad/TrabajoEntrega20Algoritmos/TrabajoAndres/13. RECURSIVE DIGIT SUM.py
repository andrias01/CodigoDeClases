"""
PROBLEMA: Dado un entero, calcular su "super digit".
El super digit se define como:
- Si el número tiene un solo dígito, ese es el super digit
- Si tiene múltiples dígitos, el super digit es el super digit de la suma de sus dígitos

EJEMPLO:
super_digit(9875) → super_digit(9+8+7+5) → super_digit(29) → super_digit(2+9) → super_digit(11) → super_digit(1+1) → 2

CASO ESPECIAL: Si se da un número n repetido k veces, primero se calcula la suma 
de los dígitos de n, se multiplica por k, y luego se encuentra el super digit.

VISUALIZACIÓN: https://cdn.programiz.com/sites/tutorial2program/files/digit-sum-recursion.png
"""

def suma_digitos_recursiva(n):
    """
    Calcula la suma de los dígitos de un número recursivamente.
    
    Args:
        n: Número entero positivo
        
    Returns:
        Suma de todos los dígitos
    """
    if n == 0:
        return 0
    return (n % 10) + suma_digitos_recursiva(n // 10)


def super_digit(n, k=1):
    """
    Calcula el super digit de un número n repetido k veces.
    
    Args:
        n: Número como string o entero
        k: Número de veces que se repite n
        
    Returns:
        El super digit
    """
    # Convertir a entero si es string
    if isinstance(n, str):
        n = int(n)
    
    # Caso base: número de un solo dígito
    if n < 10:
        return n
    
    # Calcular la suma inicial de dígitos multiplicada por k
    suma_inicial = suma_digitos_recursiva(n) * k
    
    # Aplicar recursión hasta obtener un dígito
    return super_digit(suma_inicial)


def super_digit_optimizado(n, k=1):
    """
    Versión optimizada usando la propiedad matemática de que el super digit
    es equivalente a ((n-1) % 9) + 1 para n > 0.
    
    Args:
        n: Número como string o entero
        k: Número de veces que se repite n
        
    Returns:
        El super digit
    """
    if isinstance(n, str):
        # Calcular suma de dígitos directamente del string
        suma_digitos = sum(int(digito) for digito in n)
    else:
        suma_digitos = suma_digitos_recursiva(n)
    
    suma_total = suma_digitos * k
    
    # Aplicar la fórmula matemática
    if suma_total == 0:
        return 0
    return ((suma_total - 1) % 9) + 1

# Ejemplo de uso
if __name__ == "__main__":
    casos_prueba = [
        (9875, 1),
        ("123", 3),
        (99, 1),
        ("9875", 4)
    ]
    
    for n, k in casos_prueba:
        resultado_recursivo = super_digit(n, k)
        resultado_optimizado = super_digit_optimizado(n, k)
        
        print(f"super_digit({n}, {k}):")
        print(f"  Método recursivo: {resultado_recursivo}")
        print(f"  Método optimizado: {resultado_optimizado}")
        print()