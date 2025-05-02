menu = '''
1. Depositar
2. Sacar
3. Extrato
4. Sair

Escolha uma opção: '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Valor inválido!')

    elif opcao == '2':
        valor = float(input('Informe o valor a ser sacado: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Saldo insuficiente!')
        elif excedeu_limite:
            print('Limite de saque diário ultrapassado!')
        elif excedeu_saques:
            print('Número máximo de saques diários atingido!')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Valor inválido!')

    elif opcao == '3':
        print('\n================ EXTRATO ================')
        print(extrato if extrato else 'Não foram realizadas movimentações.')
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==========================================')

    elif opcao == '4':
        break

    else:
        print('Opção inválida! Escolha novamente.')