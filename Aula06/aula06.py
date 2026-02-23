texto1= "SENAC"
print(texto1[0])
print(texto1[3])
print(texto1[-1])  #para mudar o ultimo caractere

# FUNCAO len() # a função len ela serve para ontar todos os caracteres de uma vez , espaço e considerado um cactere e uma posição.
texto2= "Ola"
print(len(texto2)) 

#FUNCAO MAI/MIN
texto3="ola mundinho"
print(texto3.upper()) #deixar a palavra maiuscula

texto4 = "OLA MUNDAO"
print(texto4.lower()) #deixar a palavra minuscula

print(texto3.capitalize())  #deixar a primeira letra Maisucula

print(texto3.title())


#No phyton quando voce quiser uma posição , sempre mandar uma posição a frente , se vc quer o 10 , coloque 11
#SUBSTRING/VOCE TEM UMA STRING E ELA QUER DIMINUIR ELA / PARTIR ELA AO MEIO 

texto5="Python"
print(texto5[0]) #retornar a letra p 
print(texto5[0:3]) #retornar as letras Pyt
print(texto5[0:4]) #retornar  as letras Pyth


#COMO SUBSTITUIR UM TEXTO PARA OUTRO // para fazer isso precisamos criar uma nova variavel nesse caso aqui foi a variavel novo_texto ,a onde tem que ter primeira a palavra antiga e a nova 

texto6 = "Hoje e aula da Heloisa"

novo_texto = texto6.replace("da Heloisa","do Jose Milton")
print(novo_texto)

#Remover o espaço em branco da string

texto7 = "  Ola mundo  "
print(texto7.strip()) #remove espaço esquerda e direita
print(texto7.lstrip()) #remove espaço da  esquerda
print(texto7.rstrip()) #remove espaço da direita

#Case sensitive = Sensivel a letras maiusculas e minusculas
texto8 = "Pulei carnaval , mas hoje estou estudando."
print("carnaval" in texto8)


print(texto8.find("estudando"))
print(texto8[31]) # e

print(texto8.count("a"))

texto9 = "Eu amo Java"
print(texto9.startswith("Eu"))
print(texto9.endswith("va"))