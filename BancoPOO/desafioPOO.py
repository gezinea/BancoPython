''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self, nome_titular):
      self.titular = nome_titular
      self.saldo = 0
      self.operacoes = []

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def depositar(self, valor):
      self.saldo += valor
      self.operacoes.append(f"+{valor}")

    # TODO: Implemente o método para realizar um saque:
    def sacar(self, valor):
        # TODO: Verifique se há saldo suficiente para o saque
         if self.saldo + valor >= 0:
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            self.saldo += valor
            self.operacoes.append(str(valor))
            # TODO: Registre a operação e retorne a  mensagem de saque negado
         else:
           print("Saque não permitido")

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    def extrato(self):
      operacoes_str = ", ".join(self.operacoes)
      print(f"operações: {operacoes_str}; Saldo: {self.saldo}")


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()