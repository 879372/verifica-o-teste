import json

def verificar_linha_preenchida(cartela, numeros_sorteados, min_numeros):
    for linha in cartela.values():
        numeros_na_linha = sum(numero in numeros_sorteados for numero in linha)
        if numeros_na_linha >= min_numeros:
            return True
    return False


cartela_json = '''
{
    "lin1": [1, 5, 19, 20, 29],
    "lin2": [38, 40, 44, 55, 58],
    "lin3": [61, 70, 75, 76, 89]
}
'''

numeros_sorteados = [5, 20, 44, 61, 70, 38, 75, 58, 61, 55]

min_numeros = 4

cartela = json.loads(cartela_json)

if verificar_linha_preenchida(cartela, numeros_sorteados, min_numeros):
    print("Uma linha foi preenchida com pelo menos 4 números!")
else:
    print("Nenhuma linha foi preenchida com pelo menos 4 números.")