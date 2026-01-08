class Cliente:
    def __init__(self, nome, cpf, telefone, endereco, servico=None, data_atendimento=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.servico = servico  # Serviço solicitado
        self.data_atendimento = data_atendimento  # Data do atendimento
    
    def __repr__(self):
        return f"Cliente({self.nome}, {self.cpf}, {self.telefone}, {self.endereco}, {self.servico}, {self.data_atendimento})"
