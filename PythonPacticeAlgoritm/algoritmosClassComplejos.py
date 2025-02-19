import time
#_________________________________________
#_________________________________________
#_________________________________________
#_________________________________________
#A. Vanya and Cards ==> de codeForces en "contests"
def min_cards_to_balance(n, x, found_cards):
    total_sum = sum(found_cards)
    
    if total_sum == 0:
        return 0  # Ya está equilibrado
    
    # Se pueden tomar cartas desde -x hasta x, así que verificamos cuántas cartas se necesitan para compensar
    needed_value = abs(total_sum)
    
    # Se necesita al menos una carta con valor igual a 'needed_value' (si existe en el rango)
    if -x <= -total_sum <= x or -x <= total_sum <= x:
        return 1
    
    # Si no se puede con una sola carta, siempre podremos hacerlo con dos como máximo
    return 2

# Lectura de entrada
#n, x = map(int, input().split())
found_cards = list(map(int, input().split()))

# Cálculo y salida del resultado
#print(min_cards_to_balance(n, x, found_cards))
#__Vanya creado por mi!!

print(abs(-8))
time.sleep(20)