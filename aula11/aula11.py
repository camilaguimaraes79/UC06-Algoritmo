import random
import math 
import datetime
numero_aleatorio = random.randint(1000, 2000)
#RANDINT > Gera apenas numeros aleatorios
print(numero_aleatorio)

#Sorteio de Aluno

alunos = ["Israel" , "Adenilson" , "Anna" , "Wellington" , "Jonathan" , "Isabelly", "João Pedro" , "Luis Felipe" , "Iara" , "Vanessa" , "Daniel", "João Paulo" , "Lucas" , "Bernado" , "Camila" , "Stefany" , "Guilherme" , "Micael", "Kauan"] 

sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)

#CHOICE escolher de forma aleatoria 

print("Duplica Dinâmica" , sorteado , " - " , sorteado2)

numero = 16 
raiz = math.sqrt(numero)
print(raiz)

#Elevar um  numero 
print(math.pow(2,2))

#Trabalhando com datas
agora = datetime.datetime.now()
print(agora.hour) #ou minutes , month , second




#Exercicio
#Solicitar ao usuario de 1 até 5
#Gerar um numero aleatorio usuando a biblioteca random.randit
#Verificar se o usuario digitou o mesmo valor que o resultado da funcao randit


numero_usuario = int(input("Digite o numero da sorte de 1 até 5:"))
numero_sorte = random.randint(1, 5)
if numero_usuario == numero_sorte:
    print("Parabéns Fulno , você ganhou um aperto de mão e dois reais")
else:
    print("Errou, tente novamente")