import time

def isPalindrome(self, x):
    x_str = str(x)  # Convertimos el número a string   O(n)
    return x_str == x_str[::-1]  # Comparamos con su versión invertida
"""
str(x) → Convertir un número a una cadena toma O(n) tiempo, donde n es el número de dígitos en x.
x_str[::-1] → Invertir la cadena también toma O(n) tiempo.
Comparación x_str == x_str[::-1] → Comparar dos cadenas de longitud n toma O(n) en el peor caso.
"""
#_____________________________________________________________
class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Si la lista está vacía, retornamos 0
            return 0

        j = 1  # `j` será el puntero para almacenar los valores únicos (comienza en 1)
        
        # Recorremos la lista desde el segundo elemento (i = 1) hasta el final
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Si encontramos un nuevo valor único
                nums[j] = nums[i]  # Guardamos el valor único en la posición j
                j += 1  # Incrementamos `j` para la siguiente posición única
        
        return j  # `j` representa la cantidad de valores únicos en nums
"""
Tiempo (O(n))
La función recorre nums una sola vez en un bucle for, por lo que la complejidad temporal es O(n), donde n es el número de elementos en nums.
Espacio (O(1))
No usamos memoria adicional aparte de unas pocas variables (j, i).
Modificamos nums en su lugar, lo que significa que la complejidad espacial es O(1).
"""
#________________________________________________________________
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Puntero para los elementos que NO son val
        
        # Recorremos la lista
        for i in range(len(nums)):
            if nums[i] != val:  # Si el elemento es diferente de val
                nums[k] = nums[i]  # Lo movemos a la posición k
                k += 1  # Incrementamos k porque encontramos un número válido
        
        return k  # Retornamos la cantidad de elementos que NO son val

# Ejemplo de uso:
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
k = solution.removeElement(nums, val)
print(k, nums[:k])  # Salida esperada: 5, [0,1,3,0,4] (el orden puede variar)
"""
Complejidad Temporal (O(n))
La función tiene un bucle for que itera sobre todos los elementos de nums una vez.
Dentro del bucle, cada elemento se compara con val y, si es diferente, se reasigna en la posición k en nums.
Ambas operaciones (comparación y reasignación) toman O(1) tiempo por elemento.
Dado que recorremos nums una sola vez, la complejidad es O(n), donde n es el número de elementos en nums.
"""
#________________________________________________________________
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []  # Si la entrada está vacía, retornamos una lista vacía
        
        # Mapeo de dígitos a letras (similar a un teclado telefónico)
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []  # Lista para almacenar las combinaciones generadas

        # Función recursiva para generar combinaciones
        def backtrack(index, current_combination):
            if index == len(digits):  # Si alcanzamos la longitud de la entrada, guardamos el resultado
                result.append("".join(current_combination))
                return
            
            current_digit = digits[index]  # Tomamos el dígito actual
            for letter in digit_to_letters[current_digit]:  # Iteramos sobre sus letras correspondientes
                backtrack(index + 1, current_combination + [letter])  # Llamada recursiva con la siguiente letra
        
        # Iniciar el proceso de backtracking desde el primer dígito
        backtrack(0, [])
        return result

# Ejemplo de uso:
solution = Solution()
print(solution.letterCombinations("23"))  
# Salida esperada: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
Tiempo (O(3ⁿ × 4ᵐ))
Cada número genera combinaciones de letras (3 para la mayoría y 4 para el 7 y el 9).
Para un digits de longitud n, la cantidad máxima de combinaciones es 3ⁿ × 4ᵐ, donde m es la cantidad de 7 u 9.
En el peor caso (9999), el tiempo es O(4⁴) = O(256).
Espacio (O(3ⁿ × 4ᵐ))
result almacena todas las combinaciones posibles.
En el peor caso, se guardan O(3ⁿ × 4ᵐ) combinaciones en memoria.
"""

time.sleep(15)
