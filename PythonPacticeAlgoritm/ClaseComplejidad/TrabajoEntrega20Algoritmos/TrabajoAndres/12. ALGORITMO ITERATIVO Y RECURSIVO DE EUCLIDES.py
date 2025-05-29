"""
PROBLEMA: Encontrar el Máximo Común Divisor (MCD) de dos números enteros.
El algoritmo de Euclides se basa en el principio: MCD(a,b) = MCD(b, a mod b)

PRINCIPIO: Si d divide tanto a 'a' como a 'b', entonces d también divide a (a mod b).

EJEMPLO: MCD(48, 18)
48 = 18 × 2 + 12  → MCD(48, 18) = MCD(18, 12)
18 = 12 × 1 + 6   → MCD(18, 12) = MCD(12, 6)
12 = 6 × 2 + 0    → MCD(12, 6) = MCD(6, 0) = 6

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/3/37/Euclid%27s_algorithm_Book_VII_Proposition_2_3.png
"""

def mcd_euclides_recursivo(a, b):
    """
    Calcula el MCD usando el algoritmo de Euclides recursivo.
    
    Args:
        a, b: Números enteros no negativos
        
    Returns:
        El máximo común divisor de a y b
        
    Complejidad: O(log(min(a,b))) tiempo, O(log(min(a,b))) espacio
    """
    # Trabajar con valores absolutos
    a, b = abs(a), abs(b)
    
    # Caso base: si b es 0, el MCD es a
    if b == 0:
        return a
    
    # Llamada recursiva con el residuo
    return mcd_euclides_recursivo(b, a % b)


def mcd_euclides_iterativo(a, b):
    """
    Calcula el MCD usando el algoritmo de Euclides iterativo.
    
    Args:
        a, b: Números enteros no negativos
        
    Returns:
        El máximo común divisor de a y b
        
    Complejidad: O(log(min(a,b))) tiempo, O(1) espacio
    """
    # Trabajar con valores absolutos
    a, b = abs(a), abs(b)
    
    # Iterar hasta que b sea 0
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    
    return a


def mcd_euclides_extendido(a, b):
    """
    Algoritmo de Euclides extendido que encuentra MCD y los coeficientes
    de la identidad de Bézout: ax + by = MCD(a,b)
    
    Args:
        a, b: Números enteros
        
    Returns:
        (mcd, x, y) donde mcd = ax + by
    """
    if a == 0:
        return b, 0, 1
    
    mcd, x1, y1 = mcd_euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return mcd, x, y

# Ejemplo de uso
if __name__ == "__main__":
    pares_prueba = [(48, 18), (17, 13), (100, 25), (7, 14)]
    
    for a, b in pares_prueba:
        mcd_rec = mcd_euclides_recursivo(a, b)
        mcd_iter = mcd_euclides_iterativo(a, b)
        mcd_ext, x, y = mcd_euclides_extendido(a, b)
        
        print(f"MCD({a}, {b}):")
        print(f"  Recursivo: {mcd_rec}")
        print(f"  Iterativo: {mcd_iter}")
        print(f"  Extendido: {mcd_ext} = {a}×{x} + {b}×{y}")
        print()