from database import conectar
from models import Cliente

# Função para inserir um cliente no banco de dados
def inserir(cliente):
    """
    Insere um novo cliente no banco de dados, incluindo o serviço solicitado e a data do atendimento.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, telefone, endereco, servico, data_atendimento) VALUES (?, ?, ?, ?, ?, ?)",
                   (cliente.nome, cliente.cpf, cliente.telefone, cliente.endereco, cliente.servico, cliente.data_atendimento))
    conexao.commit()
    conexao.close()


# Função para listar todos os clientes cadastrados
def listar():
    """
    Retorna todos os clientes cadastrados no banco de dados.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()
    return clientes

def buscar_por_cpf(cpf):
    """
    Busca um cliente pelo CPF.
    Retorna apenas um cliente, pois CPF é único.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    cliente = cursor.fetchone()
    conexao.close()
    return cliente


# Função para atualizar os dados de um cliente pelo ID
def atualizar(id, nome, cpf, telefone, endereco, servico, data_atendimento):
    """
    Atualiza os dados de um cliente existente no banco de dados.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome=?, cpf=?, telefone=?, endereco=?, servico=?, data_atendimento=? WHERE id=?",
                   (nome, cpf, telefone, endereco, servico, data_atendimento, id))
    conexao.commit()
    conexao.close()

# Função para remover um cliente pelo nome
def remover(id_cliente):
    """
    Remove um cliente do banco de dados pelo ID.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
    
    if cursor.rowcount > 0:
        conexao.commit()
        print("Cliente removido com sucesso!")
    else:
        print("Cliente não encontrado!")

    conexao.close()
