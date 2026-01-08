import sqlite3  # Importa a biblioteca SQLite integrada ao Python 

# Função para conectar ao banco de dados SQLite
def conectar():
    """
    Estabelece uma conexão com o banco de dados SQLite.
    Retorna um objeto de conexão.
    """
    return sqlite3.connect("banco.db")

# Função para verificar a versão do SQLite
def verificar_versao_sqlite():
    """
    Conecta a um banco temporário na memória e exibe a versão do SQLite.
    """
    conn = sqlite3.connect(":memory:")  # Banco de dados temporário na memória
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version();")  # Consulta a versão do SQLite
    sqlite_version = cursor.fetchone()[0]  # Obtém o resultado da consulta
    print(f"SQLite versão: {sqlite_version}")  # Exibe a versão do SQLite
    conn.close()  # Fecha a conexão com o banco

# Chama a função para exibir a versão do SQLite ao iniciar o sistema
verificar_versao_sqlite()

# Função para criar a tabela de clientes no banco de dados
def criar_tabela():
    """
    Cria a tabela 'clientes' no banco de dados se ela ainda não existir.
    """
    conexao = conectar()  # Estabelece a conexão com o banco
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

    # Criação da tabela de clientes com estrutura adequada para um cartório
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,  -- CPF como documento único
            telefone TEXT NOT NULL,
            endereco TEXT,
            servico TEXT,  -- Serviço solicitado
            data_atendimento TEXT  -- Data do atendimento
        )
    ''')

    conexao.commit()  # Confirma as alterações no banco de dados
    conexao.close()  # Fecha a conexão com o banco de dados
