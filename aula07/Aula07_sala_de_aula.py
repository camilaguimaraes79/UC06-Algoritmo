#Criar um dicionário com dados digitados pelo usuário
#Peça ao usuário: nome , idade , cidade , guarde em um dicionario e mostre na tela 

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
cidade = input("Digite sua cidade:")

pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print("Dados cadastrados:")
print(pessoa)


#Criar um dicionário com dados digitados pelo usuário 
#nome do aluno, nota1 , nota2, nota3, nota4, nota5 e depois calcule e mostre a média.

nome_aluno = input("Digite seu nome:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))
nota5 = float(input("Digite a quinta nota:"))

soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma /5

aluno = {
    "nome": nome_aluno,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "nota4": nota4,
    "nota5": nota5,
    "media": media 
}

print("Dados do aluno:")
print(aluno)
print("Média:", media)