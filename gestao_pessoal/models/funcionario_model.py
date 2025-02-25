from utils.database import GerenciadorBancoDados

class FuncionarioModel:
    def __init__(self):
        self.db = GerenciadorBancoDados()

    def criar_funcionario(self, dados):
        query = """INSERT INTO Funcionarios 
                   (nome, cpf, cargo, departamento, email, data_contratacao)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        return self.db.executar_comando(query, dados)

    def buscar_por_cpf(self, cpf):
        query = "SELECT * FROM Funcionarios WHERE cpf = %s"
        return self.db.executar_consulta(query, (cpf,))