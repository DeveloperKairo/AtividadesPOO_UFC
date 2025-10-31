from poo.banco.conta import Conta
from poo.banco.banco_lista import BancoLista


def exibir_menu():
    """Exibe o menu principal do sistema bancário"""
    print("\n" + "="*50)
    print("     SISTEMA BANCÁRIO - MENU PRINCIPAL")
    print("="*50)
    print("1.  Adicionar nova conta")
    print("2.  Remover conta")
    print("3.  Buscar conta")
    print("4.  Listar todas as contas")
    print("5.  Exibir total de contas")
    print("6.  Realizar depósito")
    print("7.  Realizar saque")
    print("8.  Realizar transferência")
    print("9.  Consultar saldo")
    print("10. Exibir histórico de transações")
    print("11. Exibir informações do banco")
    print("0.  Sair")
    print("="*50)


def adicionar_conta(banco):
    """Adiciona uma nova conta ao banco"""
    print("\n--- ADICIONAR NOVA CONTA ---")
    numero = input("Número da conta: ")
    titular = input("Nome do titular: ")
    saldo = float(input("Saldo inicial: R$ "))
    limite = float(input("Limite: R$ "))
    data_abertura = input("Data de abertura (DD/MM/AAAA): ")
    tipo_conta = input("Tipo de conta (Corrente/Poupança): ")
    
    nova_conta = Conta(numero, titular, saldo, limite, data_abertura, tipo_conta)
    banco.adicionar_conta(nova_conta)
    print(f"\n✓ Conta {numero} adicionada com sucesso!")


def remover_conta(banco):
    """Remove uma conta do banco"""
    print("\n--- REMOVER CONTA ---")
    numero = input("Número da conta a remover: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        banco.remover_conta(numero)
        print(f"\n✓ Conta {numero} removida com sucesso!")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def buscar_conta(banco):
    """Busca e exibe informações de uma conta"""
    print("\n--- BUSCAR CONTA ---")
    numero = input("Número da conta: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        print("\n--- INFORMAÇÕES DA CONTA ---")
        print(f"Número: {conta.numero}")
        print(f"Titular: {conta.titular}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print(f"Limite: R$ {conta.limite:.2f}")
        print(f"Data de abertura: {conta.data_abertura}")
        print(f"Tipo: {conta.tipo_conta}")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def realizar_deposito(banco):
    """Realiza um depósito em uma conta"""
    print("\n--- REALIZAR DEPÓSITO ---")
    numero = input("Número da conta: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        valor = float(input("Valor do depósito: R$ "))
        conta.depositar(valor)
        print(f"\n✓ Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {conta.saldo:.2f}")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def realizar_saque(banco):
    """Realiza um saque de uma conta"""
    print("\n--- REALIZAR SAQUE ---")
    numero = input("Número da conta: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        valor = float(input("Valor do saque: R$ "))
        saldo_anterior = conta.saldo
        conta.sacar(valor)
        
        if conta.saldo != saldo_anterior:
            print(f"\n✓ Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {conta.saldo:.2f}")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def realizar_transferencia(banco):
    """Realiza uma transferência entre contas"""
    print("\n--- REALIZAR TRANSFERÊNCIA ---")
    numero_origem = input("Número da conta de origem: ")
    
    conta_origem = banco.buscar_conta(numero_origem)
    if not conta_origem:
        print(f"\n✗ Conta de origem {numero_origem} não encontrada!")
        return
    
    numero_destino = input("Número da conta de destino: ")
    conta_destino = banco.buscar_conta(numero_destino)
    
    if not conta_destino:
        print(f"\n✗ Conta de destino {numero_destino} não encontrada!")
        return
    
    valor = float(input("Valor da transferência: R$ "))
    saldo_anterior = conta_origem.saldo
    conta_origem.transferir(valor, conta_destino)
    
    if conta_origem.saldo != saldo_anterior:
        print(f"\n✓ Transferência de R$ {valor:.2f} realizada com sucesso!")
        print(f"Saldo conta origem: R$ {conta_origem.saldo:.2f}")
        print(f"Saldo conta destino: R$ {conta_destino.saldo:.2f}")


def consultar_saldo(banco):
    """Consulta o saldo de uma conta"""
    print("\n--- CONSULTAR SALDO ---")
    numero = input("Número da conta: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        conta.consultar_saldo()
        print(f"Limite disponível: R$ {conta.limite:.2f}")
        print(f"Saldo total disponível: R$ {conta.saldo + conta.limite:.2f}")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def exibir_historico(banco):
    """Exibe o histórico de transações de uma conta"""
    print("\n--- HISTÓRICO DE TRANSAÇÕES ---")
    numero = input("Número da conta: ")
    
    conta = banco.buscar_conta(numero)
    if conta:
        if conta.historico_transacoes:
            print(f"\nHistórico da conta {numero}:")
            for i, transacao in enumerate(conta.historico_transacoes, 1):
                print(f"{i}. {transacao}")
        else:
            print("\nNenhuma transação realizada ainda.")
    else:
        print(f"\n✗ Conta {numero} não encontrada!")


def exibir_info_banco(banco):
    """Exibe informações do banco"""
    print("\n--- INFORMAÇÕES DO BANCO ---")
    print(f"Nome: {banco.nome}")
    print(f"Código: {banco.codigo}")
    print(f"Telefone: {banco.telefone}")
    print(f"Endereço: {banco.endereco}")
    print(f"Taxa de saque: R$ {banco.taxa_saque:.2f}")
    print(f"Taxa de transferência: R$ {banco.taxa_transferencia:.2f}")
    print(f"Total de contas: {banco.contas_totais()}")


def criar_contas_exemplo(banco):
    """Cria algumas contas de exemplo para testes"""
    conta1 = Conta("12345", "João Silva", 1000.00, 500.00, "01/10/2025", "Corrente")
    conta2 = Conta("67890", "Maria Santos", 2500.00, 1000.00, "15/10/2025", "Poupança")
    conta3 = Conta("11111", "Pedro Oliveira", 500.00, 200.00, "20/10/2025", "Corrente")
    
    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)
    banco.adicionar_conta(conta3)
    
    print("\n✓ Contas de exemplo criadas com sucesso!")


def main():
    """Função principal do sistema"""
    # Criando o banco
    banco = BancoLista(
        nome="Banco UFC Itapajé",
        codigo="001",
        telefone="0800-123-4567",
        taxa_saque=2.50,
        taxa_transferencia=5.00,
        endereco="R. Raimundo Rufino Gomes, 303 - Itapage, Itapajé - CE"
    )
    
    print("\n" + "="*50)
    print("  BEM-VINDO AO SISTEMA BANCÁRIO UFC ITAPAJÉ")
    print("="*50)
    
    # Perguntar se deseja criar contas de exemplo
    resposta = input("\nDeseja criar contas de exemplo para testes? (s/n): ")
    if resposta.lower() == 's':
        criar_contas_exemplo(banco)
    
    # Loop principal do sistema
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            adicionar_conta(banco)
        elif opcao == '2':
            remover_conta(banco)
        elif opcao == '3':
            buscar_conta(banco)
        elif opcao == '4':
            print("\n--- LISTA DE CONTAS ---")
            banco.listar_contas()
        elif opcao == '5':
            print(f"\nTotal de contas cadastradas: {banco.contas_totais()}")
        elif opcao == '6':
            realizar_deposito(banco)
        elif opcao == '7':
            realizar_saque(banco)
        elif opcao == '8':
            realizar_transferencia(banco)
        elif opcao == '9':
            consultar_saldo(banco)
        elif opcao == '10':
            exibir_historico(banco)
        elif opcao == '11':
            exibir_info_banco(banco)
        elif opcao == '0':
            print("\n" + "="*50)
            print("  Obrigado por usar o Sistema Bancário!")
            print("="*50)
            break
        else:
            print("\n✗ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
