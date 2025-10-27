class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura, tipo_conta):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.tipo_conta = tipo_conta
        self.historico_transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(f'Deposito: +{valor}')

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.historico_transacoes.append(f'Saque: -{valor}')
        else:
            print("Saldo insuficiente!")

    def transferir(self, valor, conta_destino):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico_transacoes.append(f'Transferência: -{valor} para conta {conta_destino.numero}')
        else:
            print("Saldo insuficiente para transferência!")

    def consultar_saldo(self):
        print(f'Saldo da conta {self.numero}: {self.saldo}')


class Banco:
    def __init__(self, nome, codigo, telefone, taxa_saque, taxa_transferencia, endereco):
        self.nome = nome
        self.codigo = codigo
        self.contas = []
        self.telefone = telefone
        self.taxa_saque = taxa_saque
        self.taxa_transferencia = taxa_transferencia
        self.endereco = endereco

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def remover_conta(self, numero_conta):
        self.contas = [c for c in self.contas if c.numero != numero_conta]

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        return None

    def listar_contas(self):
        for conta in self.contas:
            print(f'Conta: {conta.numero} - Titular: {conta.titular}')

    def contas_totais(self):
        return len(self.contas)
