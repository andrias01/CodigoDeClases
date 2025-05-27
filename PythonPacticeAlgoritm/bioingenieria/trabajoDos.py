# coding: utf-8
import time
from itertools import product

# Tabla de codones estándar
tabla_codones = {
    'F': ['TTT', 'TTC'], 'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'I': ['ATT', 'ATC', 'ATA'], 'M': ['ATG'], 'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'], 'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Y': ['TAT', 'TAC'], '*': ['TAA', 'TAG', 'TGA'], 'H': ['CAT', 'CAC'],
    'Q': ['CAA', 'CAG'], 'N': ['AAT', 'AAC'], 'K': ['AAA', 'AAG'],
    'D': ['GAT', 'GAC'], 'E': ['GAA', 'GAG'], 'C': ['TGT', 'TGC'],
    'W': ['TGG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG']
}

complemento = str.maketrans('ATCG', 'TAGC')

def calcular_gc_tm(secuencia):
    g = secuencia.count('G')
    c = secuencia.count('C')
    a = secuencia.count('A')
    t = secuencia.count('T')
    gc = 100 * (g + c) / len(secuencia)
    tm = 4 * (g + c) + 2 * (a + t)
    return round(gc, 2), tm

def modulo1(aminoacidos):
    """Diseño de primers desde una secuencia de 4 aminoácidos"""
    codones_posibles = [tabla_codones[aa] for aa in aminoacidos]
    primers = []
    for combinacion in product(*codones_posibles):
        forward = ''.join(combinacion)
        reverse = forward[::-1].translate(complemento)
        gc_f, tm_f = calcular_gc_tm(forward)
        gc_r, tm_r = calcular_gc_tm(reverse)
        primers.append({
            'forward': forward, 'GC_f': gc_f, 'Tm_f': tm_f,
            'reverse': reverse, 'GC_r': gc_r, 'Tm_r': tm_r
        })
    return primers

def modulo2(dna_5_3, dna_3_5, n):
    """PCR in silico con cálculo de primers y simulación"""
    primer_fwd = dna_5_3[:18]
    primer_rev = dna_5_3[-18:][::-1].translate(complemento)
    gc_f, tm_f = calcular_gc_tm(primer_fwd)
    gc_r, tm_r = calcular_gc_tm(primer_rev)
    total = n * (2 ** 2)
    return {
        'primer_forward': primer_fwd, 'GC_f': gc_f, 'Tm_f': tm_f,
        'primer_reverse': primer_rev, 'GC_r': gc_r, 'Tm_r': tm_r,
        'total_despues_2_ciclos': total
    }

def transcribir(dna):
    return dna.replace('T', 'U')

def traducir(mrna):
    aminoacidos = []
    inicio = mrna.find('AUG')
    if inicio == -1:
        return "Error: No se encontró el codón de inicio (AUG)"
    for i in range(inicio, len(mrna), 3):
        codon = mrna[i:i+3]
        if len(codon) < 3:
            break
        aa = next((k for k, v in tabla_codones.items() if codon.replace('U', 'T') in v), None)
        if aa == '*':
            break
        elif aa is None:
            return f"Error: Codón inválido {codon}"
        aminoacidos.append(aa)
    if '*' not in [k for k, v in tabla_codones.items() if any(c in mrna.replace('U', 'T') for c in v)]:
        return "Error: No se encontró codón de parada"
    return ''.join(aminoacidos)

def modulo3(dna_5_3, dna_3_5):
    """Expresión génica a partir de ADN"""
    molde = dna_3_5[::-1].translate(complemento)
    mrna = transcribir(molde)
    proteina = traducir(mrna)
    return {
        'mARN': mrna,
        'proteina': proteina
    }

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Diseño de primers (Módulo 1)")
        print("2. PCR in silico (Módulo 2)")
        print("3. Expresión génica (Módulo 3)")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            # Ejemplo input: 'MSTG'
            aminoacidos = input("Ingrese 4 aminoácidos (una letra cada uno, ej: MSTG): ").upper()
            if len(aminoacidos) != 4 or any(aa not in tabla_codones for aa in aminoacidos):
                print("Entrada inválida.")
                continue
            resultados = modulo1(aminoacidos)
            for i, res in enumerate(resultados, 1):
                print(f"\nPrimer #{i}")
                print(f"  Forward: {res['forward']}, %GC: {res['GC_f']}, Tm: {res['Tm_f']}°C")
                print(f"  Reverse: {res['reverse']}, %GC: {res['GC_r']}, Tm: {res['Tm_r']}°C")

        elif opcion == '2':
            # Ejemplo input:
            # ADN 5'->3': "ATGCGTACTAGCTAGTCGATCGATCGTAGCTAGTCG"
            # ADN 3'->5': "TACGCATGATCGATCAGCTAGCTAGCATCGATCAGC"
            dna_5_3 = input("Ingrese la cadena ADN 5'->3': ").upper()
            dna_3_5 = input("Ingrese la cadena ADN 3'->5': ").upper()
            n = int(input("Ingrese el número de cadenas iniciales: "))
            res = modulo2(dna_5_3, dna_3_5, n)
            print("\nResultados PCR in silico:")
            print(f"  Primer Forward: {res['primer_forward']}, %GC: {res['GC_f']}, Tm: {res['Tm_f']}°C")
            print(f"  Primer Reverse: {res['primer_reverse']}, %GC: {res['GC_r']}, Tm: {res['Tm_r']}°C")
            print(f"  Total de cadenas después de 2 ciclos: {res['total_despues_2_ciclos']}")

        elif opcion == '3':
            # Ejemplo input:
            # ADN 5'->3': "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
            # ADN 3'->5': "TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC"
            dna_5_3 = input("Ingrese la cadena ADN 5'->3': ").upper()
            dna_3_5 = input("Ingrese la cadena ADN 3'->5': ").upper()
            res = modulo3(dna_5_3, dna_3_5)
            print("\nResultados de expresión génica:")
            print(f"  mARN: {res['mARN']}")
            print(f"  Proteína: {res['proteina']}")

        elif opcion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú si se corre el script directamente
if __name__ == "__main__":
    menu()

time.sleep(1200)  