from crud import inserir, listar, buscar_por_cpf, atualizar, remover
from models import Cliente
from database import criar_tabela
from report import gerar_relatorio


def menu():
    """
    Exibe o menu principal do sistema.
    """
    criar_tabela()

    while True:
        print("\n==============================================")
        print("   SISTEMA DE GESTÃO – CARTÓRIO CENTRAL")
        print("==============================================\n")

        print("Serviços disponíveis:")
        print("• Registro de Imóveis")
        print("• Registro Civil (Nascimento, Casamento e Óbito)")
        print("• Reconhecimento de Firma")
        print("• Autenticação de Documentos")
        print("• Emissão de Certidões")
        print("• Protesto de Títulos\n")

        print("----------------------------------------------")
        print("Menu de Operações:")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Buscar Cliente (CPF)")
        print("[4] Atualizar Cadastro")
        print("[5] Remover Cliente")
        print("[6] Gerar Relatório")
        print("[0] Encerrar Sistema")
        print("----------------------------------------------")

        opcao = input("Escolha uma opção: ")

        # INSERIR
        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            servico = input("Serviço Solicitado: ")
            data_atendimento = input("Data do Atendimento (DD/MM/AAAA): ")

            cliente = Cliente(
                nome, cpf, telefone, endereco, servico, data_atendimento
            )
            inserir(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")

        # LISTAR
        elif opcao == '2':
            clientes = listar()

            if not clientes:
                print("Nenhum cliente encontrado.")
            else:
                for c in clientes:
                    print(
                        f"{c[0]} - {c[1]} (CPF: {c[2]}) "
                        f"- Serviço: {c[5]} | Data: {c[6]}"
                    )

        # BUSCAR POR CPF
        elif opcao == '3':
            cpf = input("Digite o CPF do cliente: ")
            cliente = buscar_por_cpf(cpf)

            if not cliente:
                print("Nenhum cliente encontrado.")
            else:
                print(
                    f"{cliente[0]} - {cliente[1]} (CPF: {cliente[2]}) "
                    f"- Serviço: {cliente[5]} | Data: {cliente[6]}"
                )

        # ATUALIZAR
        elif opcao == '4':
            id_cliente = int(input("ID do Cliente: "))
            nome = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            telefone = input("Novo Telefone: ")
            endereco = input("Novo Endereço: ")
            servico = input("Novo Serviço Solicitado: ")
            data_atendimento = input("Nova Data do Atendimento (DD/MM/AAAA): ")

            atualizar(
                id_cliente, nome, cpf, telefone,
                endereco, servico, data_atendimento
            )
            print("Cliente atualizado com sucesso!")

        # REMOVER
        elif opcao == '5':
            id_cliente = input("Digite o ID do cliente para remover: ")
            remover(id_cliente)

        # RELATÓRIO
        elif opcao == '6':
            gerar_relatorio()

        # SAIR
        elif opcao == '0':
            print("Encerrando o sistema. Obrigado por utilizar nossos serviços.")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Executa o menu
if __name__ == "__main__":
    menu()
