import re
import sys 
import time
import graphviz

class Individual:
    def __init__(self, id_num, sex, status, original_code, generation_label):
        self.id_num = id_num 
        self.sex = sex
        self.status = status 
        self.original_code = original_code
        self.generation_label = generation_label 
        if id_num is not None:
            self.unique_id = f"{generation_label}-{sex}{id_num}"
        else: 
            self.unique_id = f"{generation_label}-{sex}-Spouse-{original_code}-{id(self)}"


    def __str__(self):
        status_str = "Afectado" if self.status == 'A' else "No afectado"
        sex_str = "Hombre" if self.sex == 'M' else "Mujer"
        
        if self.id_num is None and "Spouse" in self.unique_id:
             return f"({self.original_code}): {sex_str}, {status_str}"
        
        id_display = f"Individuo {self.id_num} "
        return f"{id_display}({self.original_code}): {sex_str}, {status_str} [{self.unique_id}]"


class Union:
    def __init__(self, union_id, parent1_ref, parent2_desc_code, offspring_gen_num):
        self.id = union_id 
        self.parent1_ref = parent1_ref 
        self.parent2_desc_code = parent2_desc_code 
        self.parent2_obj = None 
        self.offspring_gen_num = offspring_gen_num 
        self.offspring = [] 

    def __str__(self):
        parent1_str = self.parent1_ref.unique_id if isinstance(self.parent1_ref, Individual) else str(self.parent1_ref)
        parent2_str = str(self.parent2_obj) if self.parent2_obj else self.parent2_desc_code
        
        offspring_details = [f"  - {str(child)}" for child in self.offspring]
        return (f"Unión {self.id}:\n"
                f"  Parental 1: {parent1_str}\n"
                f"  Parental 2: {parent2_str}\n"
                f"  Descendencia (Generación F{self.offspring_gen_num}):\n" +
                "\n".join(offspring_details))


def parse_individual_code(code_str, default_id=None, generation_label=""):
    match_full = re.match(r"([MF])(\d+)([AN])", code_str)
    match_simple = re.match(r"([MF])([AN])", code_str)

    sex, id_val, status = None, None, None

    if match_full:
        sex = match_full.group(1)
        id_str = match_full.group(2)
        status = match_full.group(3)
        id_val = int(id_str) 
    elif match_simple:
        sex = match_simple.group(1)
        status = match_simple.group(2)
        id_val = default_id 
    else:
        print(f"Advertencia de parse_individual_code: Código '{code_str}' no reconocido como individuo válido.")
        return None 

    return Individual(id_val, sex, status, code_str, generation_label)

def process_genealogy(input_str):
    lines = input_str.strip().split('\n')
    
    generations = {} 
    all_individuals_map = {} 
    unions_map = {} 

    parental_line = lines[0]
    parental_codes = parental_line.split(';')
    generations["P"] = []
    parental_id_counter = 1
    for code in parental_codes:
        if not code.strip(): continue
        ind = parse_individual_code(code, default_id=parental_id_counter, generation_label="P")
        if ind: 
            ind.unique_id = f"P-{ind.sex}{ind.id_num}" 
            generations["P"].append(ind)
            all_individuals_map[ind.unique_id] = ind
            parental_id_counter += 1
    
    for line_idx, line_content in enumerate(lines[1:]):
        parts = []
        current_segment = ""
        in_offspring_block = False
        line_stripped = line_content.strip()

        for char_idx, char in enumerate(line_stripped):
            if char == '<':
                if current_segment and current_segment[0] == 'G' and current_segment[1:].isdigit():
                     in_offspring_block = True
            elif char == '>':
                if in_offspring_block: 
                    in_offspring_block = False
            
            if char == ';' and not in_offspring_block:
                if current_segment:
                    parts.append(current_segment.strip())
                current_segment = ""
            else:
                current_segment += char
        
        if current_segment: 
            parts.append(current_segment.strip())
        
        temp_line_individuals = {} 

        for part in parts:
            if not part: continue

            offspring_match = re.match(r"(G\d+)<([^>]+)>", part)
            union_def_match = re.match(r"(\d+)([MF])([MF])([AN]):(G\d+)", part)
            individual_def_match = re.match(r"^([MF])(\d+)([AN])$", part) 

            if offspring_match:
                union_id = offspring_match.group(1)
                offspring_codes_str = offspring_match.group(2)
                offspring_codes = [c.strip() for c in re.split(r'[;,]', offspring_codes_str) if c.strip()]

                if union_id not in unions_map:
                    print(f"Advertencia: Unión {union_id} no definida antes de asignarle descendencia. Descendencia ignorada: {offspring_codes_str}")
                    continue
                
                target_union = unions_map[union_id]
                offspring_gen_label = f"F{target_union.offspring_gen_num}"
                if not generations.get(offspring_gen_label):
                    generations[offspring_gen_label] = []

                current_max_id_in_gen = 0
                if generations[offspring_gen_label]:
                    for ind_existente in generations[offspring_gen_label]:
                        if ind_existente.id_num is not None and ind_existente.id_num > current_max_id_in_gen:
                            current_max_id_in_gen = ind_existente.id_num
                
                offspring_id_counter_start = current_max_id_in_gen + 1

                for i_code in offspring_codes:
                    child = parse_individual_code(i_code, default_id=offspring_id_counter_start, generation_label=offspring_gen_label)
                    if child:
                        child.id_num = offspring_id_counter_start 
                        child.unique_id = f"{offspring_gen_label}-{child.sex}{child.id_num}"

                        target_union.offspring.append(child)
                        generations[offspring_gen_label].append(child)
                        all_individuals_map[child.unique_id] = child
                        offspring_id_counter_start +=1
            
            elif union_def_match:
                parent1_id_num_str = union_def_match.group(1)
                parent1_sex_char = union_def_match.group(2)
                parent2_sex_char = union_def_match.group(3)
                parent2_status_char = union_def_match.group(4)
                union_gid = union_def_match.group(5) 

                offspring_gen_target_num = int(union_gid[1])
                parent1_obj = None
                parent1_gen_candidate_num = offspring_gen_target_num - 1
                
                if parent1_gen_candidate_num > 0: 
                    parent1_key_filial = f"F{parent1_gen_candidate_num}-{parent1_sex_char}{parent1_id_num_str}"
                    if parent1_key_filial in all_individuals_map:
                        parent1_obj = all_individuals_map[parent1_key_filial]
                elif parent1_gen_candidate_num == 0 : 
                     parent1_key_parental = f"P-{parent1_sex_char}{parent1_id_num_str}"
                     if parent1_key_parental in all_individuals_map:
                         parent1_obj = all_individuals_map[parent1_key_parental]
                
                if not parent1_obj:
                    current_line_gen_label = f"F{line_idx + 1}"
                    if (f"F{parent1_gen_candidate_num}" == current_line_gen_label): 
                        parent1_local_key = f"{current_line_gen_label}-{parent1_sex_char}{parent1_id_num_str}"
                        if parent1_local_key in all_individuals_map: 
                             parent1_obj = all_individuals_map[parent1_local_key]

                if not parent1_obj:
                    print(f"Advertencia: Parental 1 ({parent1_sex_char}{parent1_id_num_str}) para unión {union_gid} no encontrado.")
                
                parent2_code = f"{parent2_sex_char}{parent2_status_char}"
                new_union = Union(union_gid, parent1_obj if parent1_obj else f"{parent1_sex_char}{parent1_id_num_str} (No Encontrado)", parent2_code, offspring_gen_target_num)
                
                spouse_gen_label = parent1_obj.generation_label if parent1_obj else (f"F{parent1_gen_candidate_num}" if parent1_gen_candidate_num > 0 else "P")
                
                spouse_obj = parse_individual_code(parent2_code, default_id=None, generation_label=spouse_gen_label)
                if spouse_obj:
                    new_union.parent2_obj = spouse_obj
                    if spouse_obj.unique_id not in all_individuals_map: 
                         all_individuals_map[spouse_obj.unique_id] = spouse_obj

                unions_map[union_gid] = new_union

            elif individual_def_match:
                determined_gen_num = line_idx + 1 
                gen_label = f"F{determined_gen_num}"

                if not generations.get(gen_label):
                    generations[gen_label] = []
                
                id_num_in_code = int(individual_def_match.group(2))
                ind = parse_individual_code(part, default_id=id_num_in_code, generation_label=gen_label)
                
                if ind:
                    ind.id_num = id_num_in_code 
                    ind.unique_id = f"{gen_label}-{ind.sex}{ind.id_num}"
                    
                    if ind.unique_id in all_individuals_map:
                        print(f"Advertencia: Individuo {ind.unique_id} (código: {part}) ya fue definido. Revisar entrada.")
                    
                    generations[gen_label].append(ind) 
                    all_individuals_map[ind.unique_id] = ind 
                    temp_line_individuals[f"{ind.sex}{ind.id_num}"] = ind 

            else: 
                if part.strip(): 
                    print(f"Advertencia: Segmento no reconocido o mal formado: '{part}' en la línea '{line_content}'")
            
    return generations, all_individuals_map, unions_map


def generar_arbol_grafico(generations, all_individuals_map, unions_map, filename="genealogia_arbol"):
    dot = graphviz.Digraph(comment='Árbol Genealógico', engine='dot')
    dot.attr(splines='ortho') 
    dot.attr(nodesep='0.8', ranksep='1.0') 

    generation_nodes_for_rank = {}

    for ind_id, ind in all_individuals_map.items():
        shape = 'box' if ind.sex == 'M' else 'oval' 
        style = 'filled' if ind.status == 'A' else 'solid'
        fillcolor = 'darkgray' if ind.status == 'A' else 'white'
        fontcolor = 'white' if ind.status == 'A' else 'black'
        
        label_parts = []
        if "Spouse" in ind.unique_id: 
            label_parts.append(f"{ind.original_code}")
        else: 
            label_parts.append(f"{ind.generation_label}-{ind.id_num}") 
            label_parts.append(f"({ind.original_code})")       
        
        node_label = "\n".join(label_parts)

        dot.node(ind.unique_id, label=node_label, shape=shape, style=style, fillcolor=fillcolor, fontcolor=fontcolor)

        gen_label_for_rank = ind.generation_label
        if gen_label_for_rank not in generation_nodes_for_rank:
            generation_nodes_for_rank[gen_label_for_rank] = []
        if ind.unique_id not in generation_nodes_for_rank[gen_label_for_rank]: 
             generation_nodes_for_rank[gen_label_for_rank].append(ind.unique_id)

    sorted_gen_keys = sorted(generation_nodes_for_rank.keys(), 
                             key=lambda g: -1 if g == "P" else (int(g[1:]) if g.startswith('F') else float('inf')))

    for gen_key in sorted_gen_keys:
        if generation_nodes_for_rank[gen_key]:
            with dot.subgraph() as s:
                s.attr(rank='same')
                for node_id in generation_nodes_for_rank[gen_key]:
                    s.node(node_id) 

    # Conexión explícita P -> F1
    if "P" in generations and len(generations["P"]) == 2 and \
       "F1" in generations and generations["F1"]:
        
        parent_gen_p_inds = generations["P"]
        p1_p_gen = None
        p2_p_gen = None

        if parent_gen_p_inds[0].sex == 'M' and len(parent_gen_p_inds) > 1 and parent_gen_p_inds[1].sex == 'F':
            p1_p_gen = parent_gen_p_inds[0]
            p2_p_gen = parent_gen_p_inds[1]
        elif parent_gen_p_inds[0].sex == 'F' and len(parent_gen_p_inds) > 1 and parent_gen_p_inds[1].sex == 'M':
            p1_p_gen = parent_gen_p_inds[1]
            p2_p_gen = parent_gen_p_inds[0]
        elif len(parent_gen_p_inds) == 2 : 
            p1_p_gen = parent_gen_p_inds[0]
            p2_p_gen = parent_gen_p_inds[1]

        if p1_p_gen and p2_p_gen:
            marriage_node_parental_id = "union_node_Parental_to_F1" 
            dot.node(marriage_node_parental_id, shape='diamond', label='', width='0.15', height='0.15', style='filled', color='black')
            
            dot.edge(p1_p_gen.unique_id, marriage_node_parental_id, arrowhead='none')
            dot.edge(p2_p_gen.unique_id, marriage_node_parental_id, arrowhead='none')

            sibling_connector_f1_id = "sib_conn_F1_from_P"
            dot.node(sibling_connector_f1_id, shape='point', width='0', height='0')
            dot.edge(marriage_node_parental_id, sibling_connector_f1_id, arrowhead='none')

            f1_individuals_sorted = sorted(generations["F1"], key=lambda x: x.id_num if x.id_num is not None else float('inf'))
            for i, f1_child in enumerate(f1_individuals_sorted):
                dot.edge(sibling_connector_f1_id, f1_child.unique_id, arrowhead='none')
                if i > 0: 
                    prev_f1_child_id = f1_individuals_sorted[i-1].unique_id
                    dot.edge(prev_f1_child_id, f1_child.unique_id, style='invis', constraint='true', weight='100')

    # Bucle para uniones explícitas (G21, G31, G32...)
    for union_id_str, union in unions_map.items():
        p1 = union.parent1_ref
        p2 = union.parent2_obj

        if not isinstance(p1, Individual) or not isinstance(p2, Individual):
            print(f"Advertencia de graficación: Unión {union_id_str} tiene parentales incompletos. Se omite esta unión del gráfico.")
            continue

        p1_id = p1.unique_id
        p2_id = p2.unique_id

        marriage_node_id = f"union_node_{union_id_str}" 
        dot.node(marriage_node_id, shape='diamond', label='', width='0.15', height='0.15', style='filled', color='black')
        
        dot.edge(p1_id, marriage_node_id, arrowhead='none')
        dot.edge(p2_id, marriage_node_id, arrowhead='none')
        
        if union.offspring:
            sibling_connector_id = f"sib_conn_{union_id_str}"
            dot.node(sibling_connector_id, shape='point', width='0', height='0') 
            dot.edge(marriage_node_id, sibling_connector_id, arrowhead='none')

            sorted_offspring = sorted(union.offspring, key=lambda x: x.id_num if x.id_num is not None else float('inf'))
            
            for i, child in enumerate(sorted_offspring):
                dot.edge(sibling_connector_id, child.unique_id, arrowhead='none')
                if i > 0:
                    prev_child_id = sorted_offspring[i-1].unique_id
                    dot.edge(prev_child_id, child.unique_id, style='invis', constraint='true', weight='100') 
    
    try:
        dot.render(filename, view=True, format='png', cleanup=True) 
        print(f"Árbol genealógico guardado como '{filename}.png'")
    except graphviz.backend.execute.CalledProcessError as e:
        print(f"Error al generar el gráfico con Graphviz: {e}")
        print("Asegúrate de que Graphviz esté instalado y en el PATH del sistema.")
        print("Puedes descargar Graphviz desde https://graphviz.org/download/")
        print("El código fuente DOT se imprimirá a continuación por si quieres generarlo manualmente:")
        print("------------------------- CÓDIGO DOT -------------------------")
        print(dot.source)
        print("--------------------------------------------------------------")


# --- Programa Principal ---
if __name__ == "__main__":
    codigo_entrada = """MA;FN
M1N;F2A;F3N;M4A;4MFN:G21
G21<M1N;F2N,F3A>;1MFA:G31;2FMN:G32
G31<M1N>;G32<F2A;M3N;F4N>;"""

    print("Procesando genealogía...")
    generations_data, all_individuals_data, unions_data = process_genealogy(codigo_entrada)

    print("\n--- Salida de Texto de la Genealogía ---")
    sorted_gen_labels_text = sorted(generations_data.keys(), key=lambda g: -1 if g == "P" else int(g[1:]))
    for gen_label_text in sorted_gen_labels_text:
        if gen_label_text == "P": print("Generación Parental (P):")
        else: print(f"\nGeneración Filial ({gen_label_text}):")
        
        current_gen_inds_text = sorted(generations_data[gen_label_text], key=lambda x: x.id_num if x.id_num is not None else float('inf'))
        seen_ids_text = set()
        for ind_text in current_gen_inds_text:
            if ind_text.unique_id not in seen_ids_text:
                 print(f"- {str(ind_text)}")
                 seen_ids_text.add(ind_text.unique_id)

    print("\nDetalles de Uniones Matrimoniales (Texto):")
    sorted_union_ids_text = sorted(unions_data.keys())
    for union_id_t in sorted_union_ids_text:
        print(str(unions_data[union_id_t]))

    print("\nGenerando árbol genealógico gráfico...")
    generar_arbol_grafico(generations_data, all_individuals_data, unions_data, filename="mi_arbol_genealogico_final")

    time.sleep(2000)