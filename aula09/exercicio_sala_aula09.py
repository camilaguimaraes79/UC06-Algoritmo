#Criar uma função que receba 5 notas de um aluno que calcule e retorne a média.
#Crie uma função para receber a media do aluno e retorne se ele esta aprovado ou reprovado.




def calcular_media(nota1, nota2, nota3, nota4, nota5):
    soma = nota1 + nota2 + nota3 + nota4 + nota5
    media = soma/5
    return media 

# Função que verifica aprovação
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

# Chamando as funções
media = calcular_media(nota1, nota2, nota3, nota4, nota5)
resultado = verificar_aprovacao(media)

print("Média:", media)
print("Situação:", resultado)
