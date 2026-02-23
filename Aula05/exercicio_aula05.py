numero = int(input("Digite um número de 0 a 10 para ver a tabuada: "))

if 0 <= numero <= 10:
    
    for contador in range(0, 11):
        print(numero, "x", contador, "=", numero * contador)
        
else:
    print("Erro: número inválido. Digite apenas de 0 a 10.")
    
    
