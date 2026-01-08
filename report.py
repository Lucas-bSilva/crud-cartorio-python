from crud import listar  

# Função para gerar um relatório dos clientes cadastrados no cartório
def gerar_relatorio():
    clientes = listar()
    print("\n=== RELATÓRIO DE CLIENTES DO CARTÓRIO ===")
    print(f"Total de clientes cadastrados: {len(clientes)}")
    print("ID | Nome | CPF | Telefone | Endereço | Serviço Solicitado | Data de Atendimento")
    print("-" * 100)
    for c in clientes:
        print(f"{c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]} | {c[6]}")
