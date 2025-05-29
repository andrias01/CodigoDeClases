"""
PROBLEMA: Eliminar duplicados de un array ordenado in-place, retornando la nueva longitud.
Los elementos únicos deben quedar al inicio del array.

RESTRICCIONES:
- Modificar el array in-place con O(1) memoria extra
- El orden relativo debe mantenerse
- Solo importa los primeros k elementos (donde k es la nueva longitud)

SOLUCIÓN: Técnica de dos punteros - uno lento y uno rápido.

COMPLEJIDAD: O(n) tiempo, O(1) espacio

VISUALIZACIÓN: https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png
"""

def remover_duplicados_array_ordenado(nums):
    """
    Remueve duplicados de un array ordenado in-place.
    
    Args:
        nums: Lista de enteros ordenada
        
    Returns:
        Longitud del array sin duplicados
    """
    if not nums:
        return 0
    
    # Puntero lento - posición donde colocar el siguiente elemento único
    indice_unico = 0
    
    # Puntero rápido - recorre todo el array
    for i in range(1, len(nums)):
        # Si encontramos un elemento diferente al anterior
        if nums[i] != nums[indice_unico]:
            indice_unico += 1
            nums[indice_unico] = nums[i]
    
    # La longitud del array sin duplicados
    return indice_unico + 1

# Ejemplo de uso
if __name__ == "__main__":
    array = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"Array original: {array}")
    longitud = remover_duplicados_array_ordenado(array)
    print(f"Array sin duplicados: {array[:longitud]}")
    print(f"Nueva longitud: {longitud}")