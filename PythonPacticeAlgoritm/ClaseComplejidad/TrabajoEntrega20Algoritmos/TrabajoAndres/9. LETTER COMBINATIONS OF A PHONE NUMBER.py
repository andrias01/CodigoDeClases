"""
PROBLEMA: Dado un string con dígitos 2-9, retornar todas las combinaciones posibles 
de letras que representan esos números en un teclado telefónico.

MAPEO DEL TECLADO:
2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ

EJEMPLO: "23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]

SOLUCIÓN: Backtracking recursivo para generar todas las combinaciones.

COMPLEJIDAD: O(3^n * 4^m) donde n es el número de dígitos que mapean a 3 letras 
y m es el número de dígitos que mapean a 4 letras.

VISUALIZACIÓN: https://assets.leetcode.com/uploads/2019/10/09/screen-shot-2019-10-09-at-4.28.37-pm.png
"""

def combinaciones_letras_telefono(digitos):
    """
    Genera todas las combinaciones de letras para los dígitos dados.
    
    Args:
        digitos: String de dígitos (2-9)
        
    Returns:
        Lista de todas las combinaciones posibles
    """
    if not digitos:
        return []
    
    # Mapeo del teclado telefónico
    mapeo_telefono = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    resultado = []
    
    def backtrack(indice, combinacion_actual):
        """
        Función recursiva para generar combinaciones usando backtracking.
        
        Args:
            indice: Posición actual en el string de dígitos
            combinacion_actual: Combinación de letras construida hasta ahora
        """
        # Caso base: hemos procesado todos los dígitos
        if indice == len(digitos):
            resultado.append(combinacion_actual)
            return
        
        # Obtener las letras correspondientes al dígito actual
        digito_actual = digitos[indice]
        letras = mapeo_telefono[digito_actual]
        
        # Probar cada letra posible
        for letra in letras:
            # Recursión: agregar la letra y continuar con el siguiente dígito
            backtrack(indice + 1, combinacion_actual + letra)
    
    # Iniciar el backtracking
    backtrack(0, "")
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    digitos_entrada = "23"
    combinaciones = combinaciones_letras_telefono(digitos_entrada)
    print(f"Dígitos: {digitos_entrada}")
    print(f"Combinaciones: {combinaciones}")
    print(f"Total de combinaciones: {len(combinaciones)}")