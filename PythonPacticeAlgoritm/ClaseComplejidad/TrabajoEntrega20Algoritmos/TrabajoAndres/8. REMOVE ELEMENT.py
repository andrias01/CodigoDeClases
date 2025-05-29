"""
PROBLEMA: Remover todas las instancias de un valor específico de un array in-place.
Retornar la nueva longitud del array.

RESTRICCIONES:
- Modificar el array in-place con O(1) memoria extra
- El orden de los elementos puede cambiar
- Solo importan los primeros k elementos (donde k es la nueva longitud)

SOLUCIÓN: Técnica de dos punteros para sobrescribir elementos a remover.

COMPLEJIDAD: O(n) tiempo, O(1) espacio

VISUALIZACIÓN: https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png
"""

def remover_elemento(nums, val):
    """
    Remueve todas las instancias de un valor del array in-place.
    
    Args:
        nums: Lista de enteros
        val: Valor a remover
        
    Returns:
        Nueva longitud del array
    """
    if not nums:
        return 0
    
    # Puntero que indica dónde colocar el siguiente elemento válido
    indice_valido = 0
    
    # Recorrer todo el array
    for i in range(len(nums)):
        # Si el elemento actual no es el valor a remover
        if nums[i] != val:
            nums[indice_valido] = nums[i]
            indice_valido += 1
    
    return indice_valido

# Ejemplo de uso
if __name__ == "__main__":
    array = [3, 2, 2, 3, 4, 2, 1]
    valor_remover = 2
    print(f"Array original: {array}")
    longitud = remover_elemento(array, valor_remover)
    print(f"Array después de remover {valor_remover}: {array[:longitud]}")
    print(f"Nueva longitud: {longitud}")