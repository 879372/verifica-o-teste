import json

def verificar_estado_cartela(cartelas, numeros_sorteados, min_numeros):
    cartela_kuadra = None
    cartela_kina = None
    cartela_keno = None
    
    for sorteio, numero_sorteado in enumerate(numeros_sorteados, start=1):
        for cartela_index, cartela in enumerate(cartelas):
            linhas_completas = [all(numero in numeros_sorteados[:sorteio] for numero in linha) for linha in cartela.values()]
            linhas_min_numeros = [sum(numero in numeros_sorteados[:sorteio] for numero in linha) >= min_numeros for linha in cartela.values()]
            
            if cartela_kuadra is None and any(linhas_min_numeros):
                cartela_kuadra = (cartela_index, sorteio)
            
            if cartela_kina is None and any(linhas_completas):
                cartela_kina = (cartela_index, sorteio)
            
            if cartela_keno is None and all(linhas_completas) and any(linhas_min_numeros):
                cartela_keno = (cartela_index, sorteio)
                
            if cartela_kuadra is not None and cartela_kina is not None and cartela_keno is not None:
                break
        if cartela_kuadra is not None and cartela_kina is not None and cartela_keno is not None:
            break
    
    return cartela_kuadra, cartela_kina, cartela_keno

# Cartelas em formato JSON
cartelas_json = [
    '''
    {"lin1": [1, 5, 19, 20, 29],"lin2": [38, 40, 44, 55, 58],"lin3": [61, 70, 75, 76, 90]}
    ''',
    '''
    {"lin1": [2, 6, 21, 22, 30],"lin2": [39, 41, 45, 56, 59],"lin3": [62, 71, 77, 78, 90]}
    ''',
    '''
    {"lin1": [3, 7, 22, 23, 31],"lin2": [40, 42, 46, 57, 60],"lin3": [63, 72, 78, 79, 92]}
    ''',
    '''
    {"lin1": [4, 8, 23, 24, 32],"lin2": [41, 43, 47, 58, 61],"lin3": [64, 73, 79, 80, 92]}
    ''',
    '''
    {"lin1": [5, 9, 24, 25, 33],"lin2": [42, 44, 48, 59, 62],"lin3": [65, 74, 80, 81, 93]}
    ''',
    '''
    {"lin1": [6, 10, 25, 26, 34],"lin2": [43, 45, 49, 60, 63],"lin3": [66, 75, 81, 82, 94]}
    '''
]

# Números sorteados
numeros_sorteados = [1, 5, 19, 20, 29, 38, 40, 44, 55, 58, 61, 70, 75, 76, 2, 6, 21, 22, 30, 39, 41, 45, 56, 59, 62, 71, 77, 78, 90]

# Mínimo de números na linha para considerar preenchida
min_numeros = 4

# Carregar as cartelas do formato JSON
cartelas = [json.loads(cartela) for cartela in cartelas_json]

cartela_kuadra, cartela_kina, cartela_keno = verificar_estado_cartela(cartelas, numeros_sorteados, min_numeros)

if cartela_kuadra:
    print("A kuadra foi preenchida na Cartela", cartela_kuadra[0] + 1, "no sorteio", cartela_kuadra[1])
else:
    print("A kuadra não foi preenchida.")
    
if cartela_kina:
    print("A kina foi preenchida na Cartela", cartela_kina[0] + 1, "no sorteio", cartela_kina[1])
else:
    print("A kina não foi preenchida.")

if cartela_keno:
    print("O keno foi preenchido na Cartela", cartela_keno[0] + 1, "no sorteio", cartela_keno[1])
else:
    print("O keno não foi preenchido.")
