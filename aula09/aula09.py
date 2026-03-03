
nome = "Beltrano"

#parametros sempre vão dentro do parenteses
def saudacao(nome):
    print("Olá ,",nome,"seja bem-vindo!")
    
# chamar uma funcao   
saudacao("Beltrano")

#recebe dois valores , faz a soma e retorna o resultado 
def soma(valor1, valor2):
    return valor1 + valor2

print(soma(1457, 10))

salario_funcionario = 1600
beneficio = 200
novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

#soma dois valores se a idade for igual a 18
#Senao mostrar mensagem  "Sua idade e menor que 18 ""

idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o segundo valor: "))
    resultado = soma(var1, var2)
    print("Resultado:", resultado)
else:
    print("Sua idade é menor que 18")
    
    
    
    lista = [20, 1, 6, 2, 45]
    palavra = "Ano"
    #funcao da len é retornar a quantidade de informações contidas em uma variavel 
    print(len(lista))
    print(len(palavra))
    
    #SUM- soma toda a minha lista numerica
    
    print(sum(lista))
    
    #MAX (maior valor ) / maior numero
    print(max(lista))
    
    #MIN (menor valor) /menor numero
    print("Menor" ,min( lista))
    #Ordenar /nesse caso esta colocando os numeros na ordem
    print(sorted(lista))
    
    # Tipo -Type 
    tipo = input("Digite um numero: ")
    print(type(tipo))
    
    print(float(tipo))
    #Converter o tipo
    print(int(tipo))
    
    