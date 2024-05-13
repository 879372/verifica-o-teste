import json

def verificar_linha_preenchida(cartela, numeros_sorteados):
    for linha in cartela.values():
        if all(numero in numeros_sorteados for numero in linha):
            return True
    return False

# Cartela em formato JSON
cartela_json = '''
{
    "lin1": [1, 5, 19, 20, 29],
    "lin2": [38, 40, 44, 55, 58],
    "lin3": [61, 70, 75, 76, 89]
}
'''

# Números sorteados
numeros_sorteados = [5, 38, 20, 44, 61, 70, 40, 61, 55, 76, 29]

# Carregar a cartela do formato JSON
cartela = json.loads(cartela_json)

if verificar_linha_preenchida(cartela, numeros_sorteados):
    print("Uma linha foi preenchida!")
else:
    print("Nenhuma linha foi preenchida ainda.")
