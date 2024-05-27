

CPF = input("Digite seu CPF: ")
nome = input("Digite o seu Nome: ")
datanascim = input("Digite a data do seu Nascimento (no formato DD/MM/AAAA): ")

saldo = 0
limite = 500
numero_saques = 1
extrato = ""
LIMITE_SAQUE = 3

print(f"Bem-vindo ao Banco 365, {nome}!\n")

print(f"Seu saldo é de R${saldo:.2f}. Selecione uma opção abaixo:")

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
=> """

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado. Saldo atual: R$ {saldo:.2f}.")
        else:
            print ("Digite um valor válido de depósito.")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > limite:
            print("Seu saque ultrapassa o limite de saque da sua conta.")
        
        elif valor_saque > saldo:
            print("Seu saldo não é suficitente para esta operação de saque.")

        elif numero_saques > LIMITE_SAQUE:
            print("Seu limite diário de saques foi atingido. Seu limite é de 3 saques diários.")
        
        elif valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
    
    elif opcao == "3":
        print("Extrato da Conta Corrente:")
        print(extrato)
        print(f"Seu saldo é de R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por usar o Banco 365. Até logo!")
        break
    else:
        print("Opção inválida. Escolha novamente.")
