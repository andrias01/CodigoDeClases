"""
PROBLEMA: Colocar 8 reinas en un tablero de ajedrez 8x8 de tal manera que ninguna
reina pueda atacar a otra. Las reinas atacan horizontal, vertical y diagonalmente.

REPRESENTACIÓN: Cada individuo es una lista de 8 números, donde el índice representa
la columna y el valor representa la fila donde está la reina.

OPERADORES GENÉTICOS:
- Selección: Torneo
- Cruzamiento: Cruzamiento de un punto
- Mutación: Cambio aleatorio de posición de una reina
- Función de fitness: Número de pares de reinas que no se atacan

VISUALIZACIÓN: https://upload.wikimedia.org/wikipedia/commons/1/1f/Eight-queens-animation.gif
"""

import random
import copy

class AlgoritmoGeneticoReinas:
    def __init__(self, tamaño_poblacion=100, tasa_mutacion=0.1, generaciones_max=1000):
        self.tamaño_poblacion = tamaño_poblacion
        self.tasa_mutacion = tasa_mutacion
        self.generaciones_max = generaciones_max
        self.tamaño_tablero = 8
        
    def crear_individuo_aleatorio(self):
        """Crea un individuo aleatorio (configuración de reinas)."""
        return [random.randint(0, self.tamaño_tablero - 1) for _ in range(self.tamaño_tablero)]
    
    def crear_poblacion_inicial(self):
        """Crea la población inicial aleatoria."""
        return [self.crear_individuo_aleatorio() for _ in range(self.tamaño_poblacion)]
    
    def calcular_fitness(self, individuo):
        """
        Calcula el fitness de un individuo.
        Fitness = número de pares de reinas que NO se atacan.
        Máximo fitness = 28 (C(8,2) = 8*7/2 = 28 pares posibles)
        """
        ataques = 0
        n = len(individuo)
        
        for i in range(n):
            for j in range(i + 1, n):
                # Verificar si las reinas se atacan
                if (individuo[i] == individuo[j] or  # Misma fila
                    abs(individuo[i] - individuo[j]) == abs(i - j)):  # Misma diagonal
                    ataques += 1
        
        # Máximo número de pares sin ataques menos los ataques actuales
        total_pares = n * (n - 1) // 2
        return total_pares - ataques
    
    def seleccion_torneo(self, poblacion, fitness_scores, tamaño_torneo=3):
        """Selecciona un individuo usando selección por torneo."""
        candidatos = random.sample(list(zip(poblacion, fitness_scores)), tamaño_torneo)
        return max(candidatos, key=lambda x: x[1])[0]
    
    def cruzamiento(self, padre1, padre2):
        """Realiza cruzamiento de un punto entre dos padres."""
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        return hijo1, hijo2
    
    def mutacion(self, individuo):
        """Aplica mutación a un individuo."""
        if random.random() < self.tasa_mutacion:
            individuo_mutado = copy.copy(individuo)
            posicion = random.randint(0, len(individuo) - 1)
            individuo_mutado[posicion] = random.randint(0, self.tamaño_tablero - 1)
            return individuo_mutado
        return individuo
    
    def resolver(self):
        """
        Ejecuta el algoritmo genético para resolver el problema de las 8 reinas.
        
        Returns:
            Mejor solución encontrada y su fitness
        """
        # Crear población inicial
        poblacion = self.crear_poblacion_inicial()
        
        for generacion in range(self.generaciones_max):
            # Calcular fitness de toda la población
            fitness_scores = [self.calcular_fitness(individuo) for individuo in poblacion]
            
            # Verificar si encontramos una solución perfecta
            mejor_fitness = max(fitness_scores)
            if mejor_fitness == 28:  # Solución perfecta
                mejor_individuo = poblacion[fitness_scores.index(mejor_fitness)]
                return mejor_individuo, mejor_fitness, generacion
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Mantener los mejores individuos (elitismo)
            indices_ordenados = sorted(range(len(fitness_scores)), 
                                     key=lambda i: fitness_scores[i], reverse=True)
            elite_size = self.tamaño_poblacion // 10  # 10% de elite
            for i in range(elite_size):
                nueva_poblacion.append(poblacion[indices_ordenados[i]])
            
            # Generar el resto de la población
            while len(nueva_poblacion) < self.tamaño_poblacion:
                padre1 = self.seleccion_torneo(poblacion, fitness_scores)
                padre2 = self.seleccion_torneo(poblacion, fitness_scores)
                
                hijo1, hijo2 = self.cruzamiento(padre1, padre2)
                
                hijo1 = self.mutacion(hijo1)
                hijo2 = self.mutacion(hijo2)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            # Ajustar tamaño si es necesario
            nueva_poblacion = nueva_poblacion[:self.tamaño_poblacion]
            poblacion = nueva_poblacion
            
            # Mostrar progreso cada 100 generaciones
            if generacion % 100 == 0:
                print(f"Generación {generacion}: Mejor fitness = {mejor_fitness}")
        
        # Retornar la mejor solución encontrada
        fitness_scores = [self.calcular_fitness(individuo) for individuo in poblacion]
        mejor_fitness = max(fitness_scores)
        mejor_individuo = poblacion[fitness_scores.index(mejor_fitness)]
        
        return mejor_individuo, mejor_fitness, self.generaciones_max

def imprimir_tablero_reinas(solucion):
    """Imprime el tablero con las reinas colocadas."""
    print("\nTablero de ajedrez con las 8 reinas:")
    for fila in range(8):
        linea = ""
        for columna in range(8):
            if solucion[columna] == fila:
                linea += "♛ "
            else:
                linea += ". "
        print(linea)
    print()

# Ejemplo de uso
if __name__ == "__main__":
    ag = AlgoritmoGeneticoReinas(tamaño_poblacion=200, tasa_mutacion=0.15)
    solucion, fitness, generaciones = ag.resolver()
    
    print(f"Mejor solución encontrada: {solucion}")
    print(f"Fitness: {fitness}/28")
    print(f"Generaciones: {generaciones}")
    
    if fitness == 28:
        print("¡Solución perfecta encontrada!")
        imprimir_tablero_reinas(solucion)
    else:
        print("No se encontró solución perfecta, pero esta es la mejor aproximación.")
        imprimir_tablero_reinas(solucion)