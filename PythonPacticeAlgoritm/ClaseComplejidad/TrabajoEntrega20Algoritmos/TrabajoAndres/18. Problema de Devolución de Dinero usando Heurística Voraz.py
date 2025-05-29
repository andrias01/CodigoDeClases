"""
18. Problema de Devolución de Dinero usando Heurística Voraz
===========================================================

DESCRIPCIÓN DEL PROBLEMA:
El problema de devolución de dinero consiste en encontrar la menor cantidad de monedas
necesarias para devolver una cantidad específica de dinero. La heurística voraz selecciona
siempre la moneda de mayor valor disponible que no exceda la cantidad restante por devolver.

FUNCIONAMIENTO DEL ALGORITMO:
1. Ordenar las denominaciones de monedas de mayor a menor valor
2. Para cada denominación, usar tantas monedas como sea posible sin exceder el monto restante
3. Reducir el monto restante por el valor usado
4. Repetir hasta que el monto sea cero

COMPLEJIDAD:
- Tiempo: O(n) donde n es el número de denominaciones diferentes
- Espacio: O(1) para almacenar el resultado

NOTA IMPORTANTE:
Este algoritmo es óptimo SOLO para sistemas de monedas canónicas (como EUR, USD).
Para sistemas no canónicos, puede no dar la solución óptima.

Visualización del comportamiento: https://visualgo.net/en/coinchange
"""

def devolucion_dinero_voraz(monto, denominaciones):
    """
    Resuelve el problema de devolución de dinero usando algoritmo voraz.
    
    Parámetros:
    -----------
    monto : float
        Cantidad de dinero a devolver (en la unidad más pequeña, ej: centavos)
    denominaciones : list
        Lista de valores de monedas disponibles ordenadas de mayor a menor
    
    Retorna:
    --------
    dict : Diccionario con la cantidad de cada moneda a usar
    tuple : (resultado_dict, total_monedas, es_exacto)
    """
    # Convertir a enteros para evitar problemas de punto flotante
    monto = int(round(monto * 100))  # Convertir a centavos
    denominaciones_centavos = [int(d * 100) for d in denominaciones]
    
    # Ordenar denominaciones de mayor a menor (por si no están ordenadas)
    denominaciones_centavos.sort(reverse=True)
    denominaciones_originales = sorted(denominaciones, reverse=True)
    
    resultado = {}
    monto_restante = monto
    total_monedas = 0
    
    print(f"Devolviendo: ${monto/100:.2f}")
    print(f"Denominaciones disponibles: {denominaciones_originales}")
    print("-" * 50)
    
    # Aplicar algoritmo voraz
    for i, denominacion in enumerate(denominaciones_centavos):
        if monto_restante >= denominacion:
            # Calcular cuántas monedas de esta denominación podemos usar
            cantidad_monedas = monto_restante // denominacion
            monto_usado = cantidad_monedas * denominacion
            
            # Actualizar resultado
            denominacion_original = denominaciones_originales[i]
            resultado[denominacion_original] = cantidad_monedas
            total_monedas += cantidad_monedas
            
            # Mostrar paso a paso
            print(f"Usando {cantidad_monedas} moneda(s) de ${denominacion_original}")
            print(f"Monto usado: ${monto_usado/100:.2f}")
            
            # Reducir monto restante
            monto_restante -= monto_usado
            print(f"Monto restante: ${monto_restante/100:.2f}")
            print("-" * 30)
    
    # Verificar si se pudo devolver exactamente
    es_exacto = (monto_restante == 0)
    
    return resultado, total_monedas, es_exacto

def mostrar_resultado(resultado, total_monedas, es_exacto, monto_original):
    """
    Muestra el resultado del algoritmo de forma organizada.
    """
    print("=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    
    if es_exacto:
        print(f"✅ Devolución exacta de ${monto_original:.2f}")
        print(f"Total de monedas utilizadas: {total_monedas}")
        print("\nDesglose por denominación:")
        
        for denominacion, cantidad in sorted(resultado.items(), reverse=True):
            if cantidad > 0:
                total_valor = denominacion * cantidad
                print(f"  ${denominacion} × {cantidad} = ${total_valor:.2f}")
    else:
        print("❌ No se pudo devolver la cantidad exacta con las denominaciones disponibles")

def ejemplo_sistema_canonico():
    """
    Ejemplo con sistema de monedas canónico (Euro/Dólar)
    """
    print("EJEMPLO 1: Sistema Canónico (Euro)")
    print("=" * 60)
    
    # Denominaciones del Euro (en euros)
    denominaciones_euro = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    monto_a_devolver = 6.67
    
    resultado, total_monedas, es_exacto = devolucion_dinero_voraz(monto_a_devolver, denominaciones_euro)
    mostrar_resultado(resultado, total_monedas, es_exacto, monto_a_devolver)

def ejemplo_sistema_no_canonico():
    """
    Ejemplo donde el algoritmo voraz no es óptimo
    """
    print("\n\nEJEMPLO 2: Sistema No Canónico")
    print("=" * 60)
    print("ADVERTENCIA: En este sistema, el algoritmo voraz puede no ser óptimo")
    
    # Sistema no canónico donde voraz falla
    denominaciones_especiales = [4, 3, 1]
    monto_a_devolver = 6
    
    print(f"\nCon denominaciones {denominaciones_especiales} y monto {monto_a_devolver}:")
    print("- Algoritmo voraz: 4 + 1 + 1 = 3 monedas")
    print("- Solución óptima: 3 + 3 = 2 monedas")
    
    resultado, total_monedas, es_exacto = devolucion_dinero_voraz(monto_a_devolver, denominaciones_especiales)
    mostrar_resultado(resultado, total_monedas, es_exacto, monto_a_devolver)

def comparar_con_fuerza_bruta(monto, denominaciones):
    """
    Compara el resultado voraz con una búsqueda exhaustiva (solo para montes pequeños)
    """
    from itertools import combinations_with_replacement
    
    print(f"\n\nCOMPARACIÓN CON FUERZA BRUTA para monto ${monto}")
    print("=" * 60)
    
    # Algoritmo voraz
    resultado_voraz, total_voraz, es_exacto_voraz = devolucion_dinero_voraz(monto, denominaciones)
    
    if not es_exacto_voraz:
        print("El algoritmo voraz no encontró solución exacta")
        return
    
    # Búsqueda de solución óptima por fuerza bruta (limitada)
    monto_centavos = int(round(monto * 100))
    denominaciones_centavos = [int(d * 100) for d in denominaciones]
    
    mejor_solucion = None
    min_monedas = total_voraz
    
    # Buscar todas las combinaciones posibles hasta el límite del algoritmo voraz
    for num_monedas in range(1, total_voraz + 1):
        for combinacion in combinations_with_replacement(denominaciones_centavos, num_monedas):
            if sum(combinacion) == monto_centavos:
                if num_monedas < min_monedas:
                    min_monedas = num_monedas
                    mejor_solucion = combinacion
                break
        if mejor_solucion and min_monedas < total_voraz:
            break
    
    print(f"Algoritmo voraz: {total_voraz} monedas")
    if mejor_solucion and min_monedas < total_voraz:
        print(f"Solución óptima: {min_monedas} monedas")
        print("❌ El algoritmo voraz NO es óptimo para este sistema")
    else:
        print("✅ El algoritmo voraz encontró la solución óptima")

# Ejecución principal con ejemplos
if __name__ == "__main__":
    print("ALGORITMO DE DEVOLUCIÓN DE DINERO - HEURÍSTICA VORAZ")
    print("=" * 70)
    
    # Ejemplo 1: Sistema canónico
    ejemplo_sistema_canonico()
    
    # Ejemplo 2: Sistema no canónico
    ejemplo_sistema_no_canonico()
    
    # Ejemplo 3: Comparación con fuerza bruta
    print("\n\nEJEMPLO 3: Verificación de Optimalidad")
    print("=" * 60)
    comparar_con_fuerza_bruta(6, [4, 3, 1])
    
    # Ejemplo interactivo
    print("\n\nEJEMPLO INTERACTIVO")
    print("=" * 60)
    print("Probemos con el sistema monetario colombiano:")
    
    # Sistema monetario colombiano (en pesos)
    denominaciones_col = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    monto_col = 1847
    
    resultado, total, exacto = devolucion_dinero_voraz(monto_col, denominaciones_col)
    mostrar_resultado(resultado, total, exacto, monto_col)
    
    print(f"\n📊 Visualización recomendada: https://visualgo.net/en/coinchange")
    print(f"🔗 Simulador interactivo: https://www.cs.usfca.edu/~galles/visualization/DPChange.html")