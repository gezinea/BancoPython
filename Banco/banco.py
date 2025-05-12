import textwrap

def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor a ser depositado: '))

            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor a ser sacado: '))

            saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, limite_saques=LIMITE_SAQUE)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print(f'Conta criada com sucesso! Número da conta: {conta["numero_conta"]}')

        elif opcao == '6':
            listar_contas(contas)
        
        elif opcao == '7':
            print('Saindo...')
            break

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t\tR$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        print('Valor inválido!')
    return saldo, extrato

def sacar(*, valor, saldo, extrato, numero_saques, limite, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Saldo insuficiente!')
    elif excedeu_limite:
        print('Limite de saque diário ultrapassado!')
    elif excedeu_saques:
        print('Número máximo de saques diários atingido!')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
    else:
        print('Valor inválido!')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print(extrato if extrato else 'Não foram realizadas movimentações.')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nUsuário já cadastrado!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/UF): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print(f'Usuário {nome} criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('Usuário não encontrado!')
        return None
    
def listar_contas(contas):
    if not contas:
        print('Nenhuma conta cadastrada!')
        return

    print('\n================ CONTAS =================')
    for conta in contas:
        print(f'Agência: {conta["agencia"]} | Conta: {conta["numero_conta"]} | Usuário: {conta["usuario"]["nome"]}')
    print('==========================================')
    
def menu():
    menu = '''\n
    ================ MENU =================

    1.\t Depositar
    2.\t Sacar
    3.\t Extrato
    4.\t Nova Conta 
    5.\t Listar Contas
    6.\t Novo Usuário
    7.\t Sair

    => '''
    return input(textwrap.dedent(menu))

main()