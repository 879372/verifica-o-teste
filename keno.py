import json

def verificar_cartela_totalmente_preenchida(cartela, numeros_sorteados):
    numeros_cartela = [numero for linha in cartela.values() for numero in linha]
    print(numeros_cartela)
    return all(numero in numeros_sorteados for numero in numeros_cartela)

# Cartela em formato JSON
cartela_json = '''
{
    "lin1": [1, 5, 19, 20, 29],
    "lin2": [38, 40, 44, 55, 58],
    "lin3": [61, 70, 75, 76, 89]
}
'''

# Números sorteados
numeros_sorteados = [1, 5, 19, 20, 29, 38, 40, 44, 55, 58, 61, 70, 75]

# Carregar a cartela do formato JSON
cartela = json.loads(cartela_json)

if verificar_cartela_totalmente_preenchida(cartela, numeros_sorteados):
    print("A cartela foi totalmente preenchida!", cartela)
else:
    print("A cartela ainda não foi totalmente preenchida.", numeros_sorteados)
