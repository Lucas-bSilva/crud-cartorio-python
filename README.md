# Sistema de Cadastro do Cartório Central 🏛️  

Este sistema foi desenvolvido para gerenciar clientes de um cartório, permitindo cadastro, atualização, busca, remoção e geração de relatórios.

## 📌 Funcionalidades  
- 📂 **Cadastro de Clientes** (Nome, CPF, Telefone, Endereço, Serviço, Data de Atendimento)  
- 🔍 **Busca de Clientes** pelo nome  
- 📜 **Listagem de Clientes**  
- ✏️ **Atualização de Dados do Cliente**  
- ❌ **Remoção de Clientes** pelo nome  
- 📊 **Geração de Relatórios**  

---

## 🔗 **Modelagem UML das Classes**  

```plaintext
+------------------+
|    Cliente       |
+------------------+
| - id: int       |
| - nome: str     |
| - cpf: str      |
| - telefone: str |
| - endereco: str |
| - servico: str  |
| - data_atend: str |
+------------------+
| + __init__()    |
| + exibir_dados() |
+------------------+

          |
          |  1..*  (um cliente pode estar relacionado a várias operações)
          v

+------------------+
|    CRUD         |
+------------------+
| + inserir()     |
| + listar()      |
| + buscar()      |
| + atualizar()   |
| + remover()     |
+------------------+

          |
          |  1..1  (CRUD se conecta com a Database)
          v

+------------------+
|    Database      |
+------------------+
| + conectar()     |
| + criar_tabela() |
+------------------+

          |
          |  1..*  (relacionado a vários relatórios)
          v

+------------------+
|    Relatório     |
+------------------+
| + gerar_relatorio() |
+------------------+

🛠 Tecnologias: 

Python 3.x

SQLite3 para banco de dados

VS Code para 


# Execução do Programa: 

python main.py
