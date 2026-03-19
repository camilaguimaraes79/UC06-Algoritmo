import pandas as pd 

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))

if opcao == 1:
    print("Opção 1 selecionada")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))  #usamos a idade comoum texto , porque nao vamos fazer calculos matematicos
    altura = float(input("Digite sua altura: "))
    
    dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}
    
    excel = pd.DataFrame(dados)
    excel.to_excel("Aula12\Alunos.xlsx", index=False) #SALVAR
    print("Ação Finalizada....")
    
elif opcao == 2:   #Adiconar
    print("Opção 2 selecionada...")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))  #usamos a idade comoum texto , porque nao vamos fazer calculos matematicos
    altura = float(input("Digite sua altura: "))
    
    dados = {       #guarda as informações no dicionario
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}
    
    leitura_excel = pd.read_excel("Aula12\Alunos.xlsx")
    nova_linha = len(leitura_excel)
#funcao LEN > Conta quantas linhas exixtem no excel e cria uma nova linha para receber a nova informacao digitada pelo usuario

    leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
    leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
    leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

# .loc serve para criar a nova linha / "nome", "idade" , "altura" serve para criar as colunas e = dados["nome"] , ["idade"] , ["altura"] serve para guardar os dados digitados pelo usuario

# to_excel() > servecriar uma nova planilha, pegar os dados digitados pelo usuario em formato DataFrame e gravar os dados na planilha criada
    
    leitura_excel.to_excel("Aula12\Alunos.xlsx" , index=False)
    print("Ação Finalizada....")

elif opcao == 3:
    print("Opção 3 selecionada")
    linha_apagada = int(input("Digite um número inteiro: "))
    
    #LER EXCEL
    leitura_excel = pd.read_excel("Aula12\Alunos.xlsx")
    
    #APAGAR UM DADO DO EXCEL
    leitura_excel = leitura_excel.drop(linha_apagada)
    
    #SALVAR EXCEL
    leitura_excel.to_excel("Aula12\Alunos.xlsx", index=False)
    print("Ação Finalizada....")