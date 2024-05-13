import json

# Cartelas de bingo em formato JSON
cartelas_json = '''
[
    {
        "lin1": [1, 5, 19, 20, 29],
        "lin2": [38, 40, 44, 55, 58],
        "lin3": [61, 70, 75, 76, 39]
    },
    {
        "lin1": [2, 6, 19, 21, 29],
        "lin2": [39, 40, 43, 55, 58],
        "lin3": [61, 70, 74, 71, 39]
    }
]
'''

# Números sorteados (exemplo)
numeros_sorteados = [1, 5, 19, 20, 29, 38, 40, 44, 55, 58, 61, 70, 75, 76, 39, 2]

# Convertendo a string JSON em uma lista de dicionários Python
cartelas = json.loads(cartelas_json)

# Variável para armazenar a primeira cartela com todos os números sorteados
primeira_cartela_completa = None

# Verificar qual cartela teve todos os números sorteados primeiro
for i, cartela in enumerate(cartelas, start=1):
    numeros_cartela = [numero for linha in cartela.values() for numero in linha]
    if set(numeros_sorteados).issubset(set(numeros_cartela)):
        primeira_cartela_completa = i
        break

if primeira_cartela_completa:
    print(f"A primeira cartela completa foi a número {primeira_cartela_completa}.")
else:
    print("Nenhuma cartela teve todos os números sorteados.")
