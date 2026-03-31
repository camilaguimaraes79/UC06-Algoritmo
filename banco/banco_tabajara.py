#chamar bibliotecas
import pandas as pd
import os

# nome do arquivo a ser criado
arquivo = "base_BANCO_TABAJARA.xlsx"

# criar/preencher arquivo excel
if not os.path.exists(arquivo):
    colunas = ["nome_cliente", "tipo_conta", "numero_conta", "cpf", "agencia", "extrato_bancario", "deposito", "saque"]
    df_vazio = pd.DataFrame(columns=colunas)
    df_vazio.to_excel(arquivo, index=False)

#inicio menu
while True:
    print("\n" + "="*48)
    print("        BANCO TABAJARA - SISTEMA BANCÁRIO")
    print("="*48)
    print("  1 > Criar conta")
    print("  2 > Acessar conta")
    print("  0 > Sair")

    #escolher opção
    opcao = input("Escolha uma opção: ")


    # se opção 1
    if opcao == "1":
        df_atual = pd.read_excel(arquivo)

        # dados usuário
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF: ")
        tipo = input("Digite o tipo (Corrente/Poupança/Salário): ")

        # lógica /regras
        total_clientes = len(df_atual)
        num_conta = min(0 + total_clientes, 100) # limite de 100
        agencia = min(400 + total_clientes, 700) # de 400 de 700
        extrato_inicial = 0.0 #salva numero


        #dados para o excel
        nova_linha = {
            "nome_cliente": nome,
            "tipo_conta": tipo,
            "numero_conta": num_conta,
            "cpf": cpf,
            "agencia": agencia,
            "extrato_bancario": extrato_inicial,
            "deposito": 0,
            "saque": 0
        }

        # salvar no excel
        df_atual = pd.concat([df_atual, pd.DataFrame([nova_linha])], ignore_index=True)
        df_atual.to_excel(arquivo, index=False)

        #mensagem no terminal de ok
        print("\n✅ CONTA CRIADA COM SUCESSO!")
        print(f"Cliente: {nome} | CPF: {cpf} | Tipo: {tipo}")
        print(f"Conta: {num_conta} | Agência: {agencia} | Extrato: {extrato_inicial}")

    #se opção 2
    elif opcao == "2":
        df_atual = pd.read_excel(arquivo)

        #solicita CPF e CONTA
        busca_cpf = input("Digite o CPF para acessar: ")

        # 2. Primeiro, filtramos apenas pelo CPF para ver se ele existe
        filtro_cpf = df_atual[df_atual['cpf'].astype(str) == busca_cpf]

        if not filtro_cpf.empty:
            # Se o CPF existe, agora pedimos a conta
            busca_conta = input("Agora, digite o número da conta: ")

            # Pegamos o valor da conta que está no Excel (índice 0 do filtro)
            conta_no_excel = str(filtro_cpf['numero_conta'].values[0])

            # 3. Validamos se a conta digitada bate com a do Excel
            if busca_conta == conta_no_excel:
                # Pegamos o índice (linha) real no DataFrame original
                idx = filtro_cpf.index[0]


                nome = df_atual.loc[idx, 'nome_cliente']
                tipo_conta = df_atual.loc[idx, 'tipo_conta']  # ← linha nova

                print(f"\n✅ Bem-vindo {nome} ao Banco Tabajara!")

                # ── SEGUNDA PARTE: menu interno ────────────────────────
                while True:
                    print("\n" + "="*48)
                    print("  1 > Saque")
                    print("  2 > Depósito")
                    print("  3 > Saldo")
                    print("  0 > Voltar ao menu principal")

                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "0":
                        break

                    elif opcao_conta == "1":
                        df_atual    = pd.read_excel(arquivo)
                        saldo_atual = float(df_atual.loc[idx, 'extrato_bancario'])

                        try:
                            valor_saque = float(input("Digite o valor para saque: R$ "))
                        except ValueError:
                            print(" Valor inválido. Operação encerrada.")
                            continue

                        if valor_saque <= 0:
                            print(" Número inválido, operação encerrada.")
                            continue

                        tipo_lower = str(tipo_conta).strip().lower()

                        if tipo_lower == "corrente":
                            percentual_taxa = 0.01
                            descricao_taxa  = "1% (Conta Corrente)"
                        elif tipo_lower in ["poupança", "poupanca"]:
                            percentual_taxa = 0.0
                            descricao_taxa  = "Isento (Poupança)"
                        else:
                            percentual_taxa = 0.005
                            descricao_taxa  = "0,5% (Conta Salário)"

                        taxa_valor   = round(valor_saque * percentual_taxa, 2)
                        total_debito = round(valor_saque + taxa_valor, 2)

                        if total_debito > saldo_atual:
                            print(" Valor maior que o disponível em conta.")
                            continue

                        novo_saldo = round(saldo_atual - total_debito, 2)

                        df_atual.loc[idx, 'extrato_bancario'] = novo_saldo
                        df_atual.loc[idx, 'saque'] = float(df_atual.loc[idx, 'saque']) + valor_saque
                        df_atual.to_excel(arquivo, index=False)

                        print("================================================")
                        print("      Saque realizado com sucesso!")
                        print(f"      Saque: R$ {valor_saque:.2f}")
                        print(f"      Valor em conta: R$ {novo_saldo:.2f}")
                        print(f"      Taxa para saque: {descricao_taxa}")
                        print(f"      Valor de desconto saque: R$ {taxa_valor:.2f}")
                        print("================================================\n")

                    elif opcao_conta == "2":
                        try:
                            valor_deposito = float(input("Digite o valor para depósito: R$ "))
                        except ValueError:
                            print(" Valor inválido. Operação encerrada.")
                            continue

                        if valor_deposito <= 0:
                            print(" Número inválido, operação encerrada.")
                            continue

                        df_atual    = pd.read_excel(arquivo)
                        saldo_atual = float(df_atual.loc[idx, 'extrato_bancario'])
                        novo_saldo  = round(saldo_atual + valor_deposito, 2)

                        df_atual.loc[idx, 'extrato_bancario'] = novo_saldo
                        df_atual.loc[idx, 'deposito'] = float(df_atual.loc[idx, 'deposito']) + valor_deposito
                        df_atual.to_excel(arquivo, index=False)

                        print("================================================")
                        print(f"      Valor depositado: R$ {valor_deposito:.2f}")
                        print(f"      Saldo em conta: R$ {novo_saldo:.2f}")
                        print("================================================\n")

                    elif opcao_conta == "3":
                        df_atual    = pd.read_excel(arquivo)
                        saldo_atual = float(df_atual.loc[idx, 'extrato_bancario'])
                        tipo_atual  = df_atual.loc[idx, 'tipo_conta']

                        print("================================================")
                        print(f"   Tipo conta: {tipo_atual}")
                        print(f"   Saldo em conta: R$ {saldo_atual:.2f}")
                        print("================================================\n")

                    else:
                        print(" Opção inválida.")
                # ── FIM SEGUNDA PARTE ──────────────────────────────────

            else:
                print(" Acesso negado: O número da conta não confere com o CPF.")
        else:
            print(" CPF não encontrado no sistema.")