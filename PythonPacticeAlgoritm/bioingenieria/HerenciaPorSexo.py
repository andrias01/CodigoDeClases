import time

import itertools

def calcular_probabilidades_herencia_sexual(genotipos, ligada_al_sexo=True):
    total = len(genotipos)
    frecuencia_genotipos = {}
    frecuencia_fenotipos = {}
    
    for genotipo in genotipos:
        genotipo_str = ''.join(genotipo)  # Mantenemos el orden
        if genotipo_str in frecuencia_genotipos:
            frecuencia_genotipos[genotipo_str] += 1
        else:
            frecuencia_genotipos[genotipo_str] = 1
        
        # Determinar fenotipo
        if ligada_al_sexo:
            if 'X^aX^a' in genotipo_str:
                fenotipo = "Mujer Enferma"
            elif 'X^AY' in genotipo_str:
                fenotipo = "Hombre Sano"
            elif 'X^aY' in genotipo_str:
                fenotipo = "Hombre Enfermo"
            else:
                fenotipo = "Mujer Portadora"
        else:
            sexo = "Mujer" if "XX" in genotipo_str else "Hombre"
            if "AA" in genotipo_str:
                fenotipo = f"{sexo} Tiene"
            elif "Aa" in genotipo_str:
                fenotipo = f"{sexo} Tiene" if sexo == "Mujer" else f"{sexo} No Tiene"
            else:
                fenotipo = f"{sexo} No Tiene"
        
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

def herencia_ligada_al_sexo():
    print("Selecciona la combinación de padres:")
    print("1. Mujer Sana (X^A X^A) x Hombre Sano (X^A Y)")
    print("2. Mujer Portadora (X^A X^a) x Hombre Sano (X^A Y)")
    print("3. Mujer Enferma (X^a X^a) x Hombre Sano (X^A Y)")
    print("4. Mujer Sana (X^A X^A) x Hombre Enfermo (X^a Y)")
    print("5. Mujer Portadora (X^A X^a) x Hombre Enfermo (X^a Y)")
    print("6. Mujer Enferma (X^a X^a) x Hombre Enfermo (X^a Y)")
    opcion = input("Elige una opción: ")
    
    combinaciones_dict = {
        "1": [("X^A", "X^A"), ("X^A", "Y")],
        "2": [("X^A", "X^a"), ("X^A", "Y")],
        "3": [("X^a", "X^a"), ("X^A", "Y")],
        "4": [("X^A", "X^A"), ("X^a", "Y")],
        "5": [("X^A", "X^a"), ("X^a", "Y")],
        "6": [("X^a", "X^a"), ("X^a", "Y")],
    }
    
    if opcion in combinaciones_dict:
        combinaciones = list(itertools.product(*combinaciones_dict[opcion]))
        return calcular_probabilidades_herencia_sexual(combinaciones, ligada_al_sexo=True)
    else:
        print("Opción no válida.")
        return None, None

def herencia_influenciada_por_el_sexo():
    print("Selecciona la combinación de padres:")
    print("1. Mujer AA x Hombre AA")
    print("2. Mujer Aa x Hombre AA")
    print("3. Mujer aa x Hombre AA")
    print("4. Mujer AA x Hombre Aa")
    print("5. Mujer Aa x Hombre Aa")
    print("6. Mujer aa x Hombre Aa")
    opcion = input("Elige una opción: ")
    
    combinaciones_dict = {
        "1": [("A", "A"), ("X", "X"), ("A", "A"), ("X", "Y")],
        "2": [("A", "a"), ("X", "X"), ("A", "A"), ("X", "Y")],
        "3": [("a", "a"), ("X", "X"), ("A", "A"), ("X", "Y")],
        "4": [("A", "A"), ("X", "X"), ("A", "a"), ("X", "Y")],
        "5": [("A", "a"), ("X", "X"), ("A", "a"), ("X", "Y")],
        "6": [("a", "a"), ("X", "X"), ("A", "a"), ("X", "Y")],
    }
    
    if opcion in combinaciones_dict:
        combinaciones = list(itertools.product(*combinaciones_dict[opcion]))
        return calcular_probabilidades_herencia_sexual(combinaciones, ligada_al_sexo=False)
    else:
        print("Opción no válida.")
        return None, None

def main():
    print("Selecciona el tipo de herencia genética:")
    print("1. Herencia Ligada al Sexo")
    print("2. Herencia Influenciada por el Sexo")
    opcion = input("Ingresa el número de la opción: ")
    
    if opcion == "1":
        genotipos, fenotipos = herencia_ligada_al_sexo()
    elif opcion == "2":
        genotipos, fenotipos = herencia_influenciada_por_el_sexo()
    else:
        print("Opción no válida.")
        return
    
    if genotipos and fenotipos:
        print("\nProbabilidad de genotipos:")
        for gen, prob in genotipos.items():
            print(f"{gen}: {prob:.2f}%")
        
        print("\nProbabilidad de fenotipos:")
        for fen, prob in fenotipos.items():
            print(f"{fen}: {prob:.2f}%")

if __name__ == "__main__":
    main()

time.sleep(200)


