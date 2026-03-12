# Data da entrega: 15/03/2025

# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""

# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])



# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":
]
"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""


import requests

url = "https://rickandmortyapi.com/api/character"

print("=== MENU ===")
print("1 - Consultar por ID")
print("2 - Consultar por nome")
print("3 - Lista de personagens")

opcao = int(input("Escolha uma opção: "))

# OPÇÃO 1 - CONSULTAR POR ID
if opcao == 1:
    id_personagem = int(input("Digite o ID do personagem: "))
    
    resposta = requests.get(f"{url}/{id_personagem}")
    dados = resposta.json()
    
    print("\n=== PERSONAGEM ===")
    print("ID:", dados["id"])
    print("Nome:", dados["name"])
    print("Status:", dados["status"])
    print("Espécie:", dados["species"])
    print("Gênero:", dados["gender"])
    print("Origem:", dados["origin"]["name"])
    print("Localização:", dados["location"]["name"])
    print("Imagem:", dados["image"])

# OPÇÃO 2 - CONSULTAR POR NOME
elif opcao == 2:
    nome = input("Digite o nome do personagem: ")
    
    resposta = requests.get(f"{url}/?name={nome}")
    dados = resposta.json()
    
    print("\n=== RESULTADOS ===")
    
    for personagem in dados["results"]:
        print("ID:", personagem["id"])
        print("Nome:", personagem["name"])
        print("Status:", personagem["status"])
        print("Espécie:", personagem["species"])
        print("Gênero:", personagem["gender"])
        print("Origem:", personagem["origin"]["name"])
        print("Localização:", personagem["location"]["name"])
        print("Imagem:", personagem["image"])
        print("-----------------------")

# OPÇÃO 3 - LISTAR PERSONAGENS
elif opcao == 3:
    resposta = requests.get(url)
    dados = resposta.json()
    
    print("\n=== LISTA DE PERSONAGENS ===")
    
    for personagem in dados["results"]:
        print("ID:", personagem["id"])
        print("Nome:", personagem["name"])
        print("Status:", personagem["status"])
        print("Espécie:", personagem["species"])
        print("Gênero:", personagem["gender"])
        print("Origem:", personagem["origin"]["name"])
        print("Localização:", personagem["location"]["name"])
        print("Imagem:", personagem["image"])
        print("-----------------------")

else:
    print("Opção inválida.")