# a função faz com que a variavel que foi associada a input permita adicionar uma informação para que depois use a variavel no print, segue exemplo
nome = input("Digite o seu nome: ")
print("Seu nome é:" , nome)
    
# indenpendente do que você digitar, o input vai transformar aquilo em texto, mesmo se for número
"""
Devido a isso, teremos que passar a especificar o tipo que estou digitando, como nùmero ou texto,
para que assim o seistassim o código fique de acordo e apresente aquilo que é necessário exemplo: Int = inteiro // #float = decimais
"""
    
""" Exemplo de erro abaixo sem a especificação do tipo
# numeros = input("Digite um numero de 1 a 10")
# soma = numeros + 10
# print("soma")"""
    
# Exemplo com a especificação do tipo
numeros = int(input("Digite um numero de 1 a 10: "))
soma = numeros + 10 # "5" + 10
print(soma)

calculo_salario = float(input("Digite o seu salario: "))
soma_salario = calculo_salario * 3.5
print(soma_salario)


# a gente nao usa chaves no python usa identação ( e o espaçamento ) e muito importante se não o python55 não executa , no lugar de chaves se usa : 


idade = 20

if idade >= 18: #true #porque 20 e maior que 18
    print("Sua idade é : ", idade) #Identação
    
    
    # IF - ELSE
    valida_idade = int(input("Digite sua idade")) #com esse codigo não precisa ficar alterando o codigo 
    if valida_idade < 18: #false / vai mostrar a 2 mensagem
        input("Você é menor de idade e precisa da presença dois pais")
        
    else:
        print("Você é maior de idade , pode entrar!")
        
        
        
        #IF  - ELIF - ELSE 
        nota = int(input("Digite a nota do aluno "))
        nome_aluno = input("Digite o nome do aluno ")
        
        if nota >= 9:
            print("O aluno {nome_aluno} está Aprovado com a nota {nota}")     #print(f"O aluno {nome_aluno} está Aprovado com a nota {nota}") # esse f não e obrigatorio e so uma maneira de fazer 
        elif nota >= 7 and nota <= 8:

            print("O aluno {nome_aluno} está Aprovado por conselho com a nota {nota}")   
            
        else:
            print(f"O aluno {nome_aluno} está Reprovado com a nota {nota}")
            
            
            #Se o usuario for menor de idade então ele precisa ter autorização.
            #Se o usuario for maior de idade , ele precisa ter a altura  minima
            
            idade_cliente = int(input("Digite a idade do cliente :"))
            altura_cliente = float(input("Digite a altura do cliente "))
            
            if idade_cliente < 18:
                print("O cliente é menor de idade e não pode entrar no brinquedo")
            else:
                if altura_cliente >= 1.50: #false
                    print("Você é maior de idade e  tem a altura minima para o brinquedo ")
                else:
                    print("Você mesmo sendo maior de idade  , tem menos de 1.50 de altura e não pode ir ao brinquedo")
                    
                # print("Cliente maior idade pode subir no brinquedo ")
                
                
            # o operador ternario a função é so diminuir / deixar mais enchuto
            
            
            #IF/ELSE
            valida_idade = 37
            #CONDICIONAL ENCADEADA
            status = "menor de idade" if valida_idade < 18 else "maior de idade"
            print(status)
            
            #condicionais if e else , variaveis e input
           # if elif e else
           #