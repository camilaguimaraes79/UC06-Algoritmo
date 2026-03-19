#Bixar a extensao View para abrir as colunas


import pandas as pd # O pd e um apelido que damos para a biblioteca , podemos chamar o apelido no codigo , inves de digitar pandas 

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))  #usamos a idade comoum texto , porque nao vamos fazer calculos matematicos
altura = float(input("Digite sua altura: "))
#Dicionario , para o diferencia ro dicionario de uma lista é dicionarios usamos {} e lista usamos []
#Criação de um dicionario para receber os dados digitados pelo usuario

dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}
# #DataFrame e a criação de um excel no formato que o Pandas entende para trabalhar com dados
# excel = pd.DataFrame(dados)

# to _excel() > serve para criar uma nova planilhas , pegar os dados digitados pelo usuario em formato DataFrame e gravar na planilha criada

#excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)

#Ler o excel 

leitura_excel = pd.read_excel("Aula12\cadastro_alunos.xlsx")
nova_linha = len(leitura_excel)
# #funcao LEN > Conta quantas linhas exixtem no excel e cria uma nova linha para receber a nova informacao digitada pelo usuario

# leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
# leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
# leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

 #Salvar
# leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)

# print(leitura_excel["idade"])

#APAGAR LINHAS DE UMA PLANILHA 

#leitura_excel = leitura_excel.drop(5)


leitura_excel.loc[4, "nome"] = dados["nome"]
leitura_excel.loc[4, "idade"] = dados["idade"]
leitura_excel.loc[4, "altura"] = dados["altura"]

#Salvar
leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False) #SALVAR
