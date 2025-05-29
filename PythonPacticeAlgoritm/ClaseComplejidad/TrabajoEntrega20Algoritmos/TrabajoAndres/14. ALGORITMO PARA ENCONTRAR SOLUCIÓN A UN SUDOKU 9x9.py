"""
PROBLEMA: Resolver un puzzle de Sudoku 9x9.
REGLAS:
- Cada fila debe contener dígitos del 1-9 sin repetición
- Cada columna debe contener dígitos del 1-9 sin repetición  
- Cada subcuadro 3x3 debe contener dígitos del 1-9 sin repetición
- Los ceros representan celdas vacías

TÉCNICA: Backtracking con poda (constraint satisfaction)

COMPLEJIDAD: O(9^m) donde m es el número de celdas vacías

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/f/ff/Sudoku-by-L2G-20050714.svg
"""

def es_valido_sudoku(tablero, fila, columna, numero):
    """
    Verifica si es válido colocar un número en una posición específica.
    
    Args:
        tablero: Matriz 9x9 representando el sudoku
        fila: Fila donde colocar el número
        columna: Columna donde colocar el número
        numero: Número a colocar (1-9)
        
    Returns:
        True si es válido, False en caso contrario
    """
    # Verificar fila
    for col in range(9):
        if tablero[fila][col] == numero:
            return False
    
    # Verificar columna
    for fil in range(9):
        if tablero[fil][columna] == numero:
            return False
    
    # Verificar subcuadro 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == numero:
                return False
    
    return True


def encontrar_celda_vacia(tablero):
    """
    Encuentra la primera celda vacía en el tablero.
    
    Args:
        tablero: Matriz 9x9 del sudoku
        
    Returns:
        (fila, columna) de la celda vacía, o None si no hay celdas vacías
    """
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return None


def resolver_sudoku(tablero):
    """
    Resuelve un sudoku usando backtracking.
    
    Args:
        tablero: Matriz 9x9 con el sudoku a resolver (se modifica in-place)
        
    Returns:
        True si se encontró solución, False si no tiene solución
    """
    # Buscar la primera celda vacía
    celda_vacia = encontrar_celda_vacia(tablero)
    
    # Si no hay celdas vacías, el sudoku está resuelto
    if celda_vacia is None:
        return True
    
    fila, columna = celda_vacia
    
    # Probar números del 1 al 9
    for numero in range(1, 10):
        if es_valido_sudoku(tablero, fila, columna, numero):
            # Colocar el número
            tablero[fila][columna] = numero
            
            # Recursión: intentar resolver el resto
            if resolver_sudoku(tablero):
                return True
            
            # Backtrack: deshacer el movimiento
            tablero[fila][columna] = 0
    
    # No se encontró solución
    return False


def imprimir_sudoku(tablero):
    """
    Imprime el tablero de sudoku de forma legible.
    
    Args:
        tablero: Matriz 9x9 del sudoku
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        
        print()

# Ejemplo de uso
if __name__ == "__main__":
    # Sudoku de ejemplo (0 representa celdas vacías)
    sudoku_ejemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Sudoku inicial:")
    imprimir_sudoku(sudoku_ejemplo)
    print("\nResolviendo...\n")
    
    if resolver_sudoku(sudoku_ejemplo):
        print("Sudoku resuelto:")
        imprimir_sudoku(sudoku_ejemplo)
    else:
        print("No se encontró solución para este sudoku.")