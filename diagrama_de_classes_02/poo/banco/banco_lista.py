class BancoLista:
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
        if not self.contas:  # Verifica se a lista está vazia
            print("Nenhuma conta cadastrada.")
        else:
            for conta in self.contas:
                print(f'Conta: {conta.numero} - Titular: {conta.titular}')

    def contas_totais(self):
        return len(self.contas)
