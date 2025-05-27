import time

import itertools

def calcular_probabilidades(genotipos):
    """ Calcula la probabilidad de cada genotipo y fenotipo en un cruce genético."""
    total = len(genotipos)
    frecuencia_genotipos = {}
    frecuencia_fenotipos = {}
    
    for genotipo in genotipos:
        genotipo_str = ''.join(sorted(genotipo))  # Ordenamos para evitar duplicados como "Aa" y "aA"
        if genotipo_str in frecuencia_genotipos:
            frecuencia_genotipos[genotipo_str] += 1
        else:
            frecuencia_genotipos[genotipo_str] = 1
            
        # Fenotipo: Solo se expresa el recesivo si es "aa"
        fenotipo = "Dominante" if 'A' in genotipo_str else "Recesivo"
        if fenotipo in frecuencia_fenotipos:
            frecuencia_fenotipos[fenotipo] += 1
        else:
            frecuencia_fenotipos[fenotipo] = 1
    
    # Convertimos a porcentaje
    for key in frecuencia_genotipos:
        frecuencia_genotipos[key] = (frecuencia_genotipos[key] / total) * 100
    for key in frecuencia_fenotipos:
        frecuencia_fenotipos[key] = (frecuencia_fenotipos[key] / total) * 100
    
    return frecuencia_genotipos, frecuencia_fenotipos

def herencia_uniformidad():
    """ Cruce AA x aa """
    padres = [("A", "A"), ("a", "a")]
    combinaciones = list(itertools.product(*padres))
    return calcular_probabilidades(combinaciones)

def herencia_segregacion():
    """ Cruce Aa x Aa """
    padres = [("A", "a"), ("A", "a")]
    combinaciones = list(itertools.product(*padres))
    return calcular_probabilidades(combinaciones)

def herencia_independiente():
    """ Cruce AaBb x AaBb """
    padres = [("A", "a"), ("A", "a"), ("B", "b"), ("B", "b")]
    combinaciones = list(itertools.product(*padres))
    total = len(combinaciones)
    frecuencia_genotipos = {}
    frecuencia_fenotipos = {}
    
    for genotipo in combinaciones:
        genotipo_ordenado = ''.join(sorted(genotipo))
        if genotipo_ordenado in frecuencia_genotipos:
            frecuencia_genotipos[genotipo_ordenado] += 1
        else:
            frecuencia_genotipos[genotipo_ordenado] = 1
            
        # Fenotipos: Solo es recesivo si es "aa" o "bb"
        fenotipo_A = "Dominante" if 'A' in genotipo_ordenado else "Recesivo"
        fenotipo_B = "Dominante" if 'B' in genotipo_ordenado else "Recesivo"
        fenotipo = f"{fenotipo_A} - {fenotipo_B}"
        
        if fenotipo in frecuencia_fenotipos:
            frecuencia_fenotipos[fenotipo] += 1
        else:
            frecuencia_fenotipos[fenotipo] = 1
    
    # Convertimos a porcentaje
    for key in frecuencia_genotipos:
        frecuencia_genotipos[key] = (frecuencia_genotipos[key] / total) * 100
    for key in frecuencia_fenotipos:
        frecuencia_fenotipos[key] = (frecuencia_fenotipos[key] / total) * 100
    
    return frecuencia_genotipos, frecuencia_fenotipos

def main():
    print("Selecciona el tipo de herencia genética:")
    print("1. Herencia de uniformidad (AA x aa)")
    print("2. Herencia de segregación independiente (Aa x Aa)")
    print("3. Herencia independiente (AaBb x AaBb)")
    opcion = input("Ingresa el número de la opción: ")
    
    if opcion == "1":
        genotipos, fenotipos = herencia_uniformidad()
    elif opcion == "2":
        genotipos, fenotipos = herencia_segregacion()
    elif opcion == "3":
        genotipos, fenotipos = herencia_independiente()
    else:
        print("Opción no válida.")
        return
    
    print("\nProbabilidad de genotipos:")
    for gen, prob in genotipos.items():
        print(f"{gen}: {prob:.2f}%")
    
    print("\nProbabilidad de fenotipos:")
    for fen, prob in fenotipos.items():
        print(f"{fen}: {prob:.2f}%")

if __name__ == "__main__":
    main()


time.sleep(200)


