menu = """
Escolha uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
      valor = float(input("Digite o valor a ser depositado: "))
      if valor > 0:
        saldo = saldo + valor
        print("Depósito realizado com sucesso!")
      else:
        print("Valor inválido!")
    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))
        if numero_saque < LIMITE_SAQUES:
          if valor > 0 and valor <= 500:
              if saldo >= valor:
                  saldo -= valor
                  numero_saque = numero_saque + 1
                  print("Saque realizado com sucesso!")
              else:
                  print("Saldo insuficiente!")
          else:
              print("Valor inválido!")
        else:
          print("Limite de saques diários atingido!")
    elif opcao == "e":
        print(f"Seu saldo é: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada!")
