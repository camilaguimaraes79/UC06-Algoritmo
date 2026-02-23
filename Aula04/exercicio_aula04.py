#Exercicio 1

#Crie um algoritmo que leia dois números inteiros e verifique qual é maior e qual é o menor e imprima o resultado no console no terminal 

numero_1 = int(input("Digite um  número de 1 á 20:"))
numero_2 = int(input("Digite um número de 1 á 15 :"))

if numero_1 > numero_2:
    print("O primeiro é maior  ")
    
else:
    print("Segundo é maior ")
    
    
    #Exercicio número 02 / Estações do Ano
    
    
    #Crie um algoritmo onde o usuário digita um número de 1 até 12 e retorne em tela qual é o mês correspondente a ele:
    
 numero = int(input("Digite um número de 1 a 12: "))

if numero <= 0:
    print("Número inválido")
elif numero > 12:
    print("Número inválido")
elif numero == 1:
    print("Janeiro")
elif numero == 2:
    print("Fevereiro")
elif numero == 3:
    print("Março")
elif numero == 4:
    print("Abril")
elif numero == 5:
    print("Maio")
elif numero == 6:
    print("Junho")
elif numero == 7:
    print("Julho")
elif numero == 8:
    print("Agosto")
elif numero == 9:
    print("Setembro")
elif numero == 10:
    print("Outubro")
elif numero == 11:
    print("Novembro")
else:
    print("Dezembro")



        
        # Crie um programa em Python que receba um número inteiro do usuário e determine : É par ou é ímpar? o programa deve exibir na tela se o númeroinformado e ímpar ou par 
        
        
        
        
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")


