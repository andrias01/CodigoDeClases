"""
Problema B: Expresión de Edad (Dr. O y sus 2 nietas Alyssa y Konari)

DESCRIPCIÓN DEL PROBLEMA:
El Dr. O tiene dos nietas: Alyssa y Konari. El problema típicamente involucra
encontrar las edades actuales o futuras basándose en relaciones matemáticas
entre sus edades.

PROBLEMA ESPECÍFICO:
- La edad del Dr. O es el doble de la suma de las edades de sus nietas
- Alyssa es 3 años mayor que Konari
- En 5 años, la edad del Dr. O será igual a la suma de las edades futuras de sus nietas más 10

Encontrar las edades actuales de todos.

SOLUCIÓN:
Utilizamos un sistema de ecuaciones para resolver el problema:
- Sea k = edad de Konari
- Alyssa = k + 3
- Dr. O = 2 * (k + k + 3) = 2 * (2k + 3) = 4k + 6

En 5 años:
- Dr. O + 5 = (k + 5) + (k + 3 + 5) + 10
- 4k + 6 + 5 = k + 5 + k + 8 + 10
- 4k + 11 = 2k + 23
- 2k = 12
- k = 6

Visualización: https://www.geogebra.org/calculator (para gráficos de ecuaciones)
"""

def resolver_edades():
    """
    Resuelve el problema de las edades del Dr. O y sus nietas
    
    Returns:
        tuple: (edad_konari, edad_alyssa, edad_dr_o)
    """
    # Resolviendo el sistema de ecuaciones
    # k = edad de Konari
    # Alyssa = k + 3
    # Dr. O = 4k + 6
    # Ecuación: 4k + 11 = 2k + 23
    
    # 4k - 2k = 23 - 11
    # 2k = 12
    # k = 6
    
    edad_konari = 6
    edad_alyssa = edad_konari + 3
    edad_dr_o = 4 * edad_konari + 6
    
    return edad_konari, edad_alyssa, edad_dr_o

def verificar_condiciones(edad_konari, edad_alyssa, edad_dr_o):
    """
    Verifica que las edades cumplan todas las condiciones del problema
    
    Args:
        edad_konari (int): Edad actual de Konari
        edad_alyssa (int): Edad actual de Alyssa
        edad_dr_o (int): Edad actual del Dr. O
    
    Returns:
        bool: True si todas las condiciones se cumplen
    """
    print("=== VERIFICACIÓN DE CONDICIONES ===")
    
    # Condición 1: Dr. O es el doble de la suma de las edades de sus nietas
    suma_nietas = edad_alyssa + edad_konari
    condicion1 = edad_dr_o == 2 * suma_nietas
    print(f"Condición 1: Dr. O ({edad_dr_o}) = 2 × (Alyssa + Konari) = 2 × {suma_nietas} = {2 * suma_nietas}")
    print(f"¿Se cumple? {condicion1}")
    
    # Condición 2: Alyssa es 3 años mayor que Konari
    condicion2 = edad_alyssa == edad_konari + 3
    print(f"Condición 2: Alyssa ({edad_alyssa}) = Konari + 3 = {edad_konari} + 3 = {edad_konari + 3}")
    print(f"¿Se cumple? {condicion2}")
    
    # Condición 3: En 5 años, Dr. O = suma de nietas + 10
    dr_o_futuro = edad_dr_o + 5
    suma_nietas_futuro = (edad_alyssa + 5) + (edad_konari + 5)
    condicion3 = dr_o_futuro == suma_nietas_futuro + 10
    print(f"Condición 3: En 5 años, Dr. O ({dr_o_futuro}) = suma nietas ({suma_nietas_futuro}) + 10 = {suma_nietas_futuro + 10}")
    print(f"¿Se cumple? {condicion3}")
    
    return condicion1 and condicion2 and condicion3

def main():
    """
    Función principal para resolver y mostrar el problema de edades
    """
    print("=== PROBLEMA B: EXPRESIÓN DE EDAD ===")
    print("Dr. O y sus nietas Alyssa y Konari")
    print("\nCondiciones del problema:")
    print("1. La edad del Dr. O es el doble de la suma de las edades de sus nietas")
    print("2. Alyssa es 3 años mayor que Konari")
    print("3. En 5 años, la edad del Dr. O será igual a la suma de las edades futuras de sus nietas más 10")
    
    # Resolver el problema
    edad_konari, edad_alyssa, edad_dr_o = resolver_edades()
    
    # Mostrar resultados
    print(f"\n=== SOLUCIÓN ===")
    print(f"Edad actual de Konari: {edad_konari} años")
    print(f"Edad actual de Alyssa: {edad_alyssa} años")
    print(f"Edad actual del Dr. O: {edad_dr_o} años")
    
    # Verificar que la solución es correcta
    print()
    es_correcta = verificar_condiciones(edad_konari, edad_alyssa, edad_dr_o)
    
    if es_correcta:
        print("\n✅ ¡Todas las condiciones se cumplen! La solución es correcta.")
    else:
        print("\n❌ Error: Alguna condición no se cumple.")
    
    # Mostrar proyección a futuro
    print(f"\n=== EN 5 AÑOS ===")
    print(f"Konari tendrá: {edad_konari + 5} años")
    print(f"Alyssa tendrá: {edad_alyssa + 5} años")
    print(f"Dr. O tendrá: {edad_dr_o + 5} años")

if __name__ == "__main__":
    main()