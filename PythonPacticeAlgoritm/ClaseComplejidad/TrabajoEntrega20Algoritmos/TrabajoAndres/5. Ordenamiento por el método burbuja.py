"""
PROBLEMA: Ordenar una lista de elementos de menor a mayor utilizando el algoritmo burbuja.

EXPLICACIÓN DEL ALGORITMO:
El algoritmo burbuja compara elementos adyacentes y los intercambia si están en orden 
incorrecto. Este proceso se repite hasta que no se necesiten más intercambios.
Es llamado "burbuja" porque los elementos más pequeños "burbujean" hacia arriba.

COMPLEJIDAD: O(n²) en el peor caso, O(n) en el mejor caso (lista ya ordenada)

VISUALIZACIÓN: https://visualgo.net/en/sorting
"""

def ordenamiento_burbuja(lista):
    """
    Ordena una lista usando el algoritmo de ordenamiento burbuja.
    
    Args:
        lista: Lista de elementos comparables
        
    Returns:
        Lista ordenada de menor a mayor
    """
    n = len(lista)
    lista_copia = lista.copy()  # No modificar la lista original
    
    # Recorrer todos los elementos
    for i in range(n):
        intercambio = False  # Optimización: detectar si ya está ordenada
        
        # Los últimos i elementos ya están en su posición correcta
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento actual es mayor que el siguiente
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break
            
    return lista_copia

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {numeros}")
    print(f"Lista ordenada: {ordenamiento_burbuja(numeros)}")