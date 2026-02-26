#criando um dicionário
pessoa = {
    "nome": "Ana",
    "idade": "25",
    "cidade" : "São Paulo"
    
}

#acessando



#Dicionário em Python

aluno = {
    "nome_aluno": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "TÉCNICO EM INFORMÁTICA PARA INTERNET",
    
    # Lista (Array em Python é lista)
    "Array": [30, True, "Texto"],
           #   0    1       2
    # Dicionário dentro de outro
    "endereco": {
        "cidade": "SP",       
        "estado": "SP",
        "numero": "234" 
    }
}
#mostra o dicionario principal
print(aluno)
#retorna o nome aluno
print(aluno["nome_aluno"])
#retorna o array
print(aluno["Array"])
#retorna o endereco , estamos acessando um dicionario dentro de outro dicionario
print(aluno["endereco"])

#acessar apenas um unico dado do endereco
print(aluno["endereco"]["estado"]) #o segundo colchete e para acessar o dado que quiser

#acessando campo especifico dentro de um array
print(aluno ["Array"][1])

#ALTERAR DADOS DO DICIONARIO
aluno["idade"] = 20
print(aluno["idade"])

#Alterar dados dentro de um array que está dentro do dicionario
aluno["Array"][2] = 9
print(aluno["Array"])

#Alterar dados do dicionario endereco que esta dentro do dicionario
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"])
print(aluno["endereco"]["cidade"])

#Sempre que precisar acessar uma chave dentro de um dicionario usamos colchetes

#ADICIONAR UM NOVO CAMPO 
aluno["periodo"] = "Noturno"
print(aluno)

#Para deletar uma informação usamos a palavra del

del aluno["idade"] 
print(aluno)

#deletar mais de uma informação na mesma linha
del aluno["endereco"] ,aluno["curso"]
print(aluno)

#percorrer um dicionario usando laco de repetição 
for chave in aluno:
    print(chave)
    

#percorrer um dicionario usando laco de repetição para retornar os valores
for valor in aluno.values():
    print(valor)
    
    
    #percorrer um dicionario e retornar chave e valor 
    
    for chave, valor in aluno.items():
        print(chave, ":", valor)
        