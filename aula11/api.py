import requests

#API
url = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url) #retorno status 200

json = resposta.json() #retornar o JSON

print(json)

personagem = json["results"] #Consultar os meus personagens

print(personagem)

#laço de repetição para consultar apenas os nomes dos personagens

for nome_personagem in personagem:
    print(nome_personagem["name"])
    
    
    #Retornar mais imformações além do nome
    for mais_info in personagem:
        print("Nome: ", mais_info["name"])
        print("Status: ", mais_info["status"])
        print("Especie: ", mais_info["species"])
        print("-------------------------------")
    
    #Pedir ao usuario para digitar um ID e retornar da API o personagem referente a esse ID
    
    id = int(input("Digite um número inteiro: "))
    
    link_API = f"https://rickandmortyapi.com/api/character/={id}"
    
    resposta = requests.get(link_API)
    
    novo_json = resposta.json()
    
    print("Nome:" , novo_json["name"])
    print("Status:" ,novo_json["status"])
    print("Especie:" , novo_json["species"])
    print("-------------------------------")
    
    #Data de entrega: 15/03/2026
    #  Criar um menu para a seleção 
    # 1 - Consultar por ID
    # 2 - Consultar por nome
    # Lista de personagens
    
    #OPÇÃO 1
    """
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
    """
    
    #Se selecionar a opção 2:
    """
    Pedir ao usuario para digitar um nome e retornar de dentro da API o personagem referente ao nome digitado
    
    OBS de Codigo : para percorrer o json e retornar
    

    """
    #for personagem in dados ["results"]:
    # print(personagem["name"])
    
    
    #Se selecionar a opção 3:
    
    #Retornar todos os personagens
    #Lista das informações que deverão ser retornadas:
    
    