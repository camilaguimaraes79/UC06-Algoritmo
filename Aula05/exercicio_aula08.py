numero_digitado = int(input("Digite um número de 1 a 10: "))

if 1 <= numero_digitado <= 10:
    print("Tabuada do:", numero_digitado)

    for i in range(0, 11):
        resultado = numero_digitado * i
        print(f"{numero_digitado} x {i} = {resultado}")

else:
    print("Erro: o valor é inválido.")
1