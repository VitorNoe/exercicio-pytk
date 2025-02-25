from utils.database import GerenciadorBancoDados

class ContratoModel:
    def __init__(self):
        self.db = GerenciadorBancoDados()
    
    def criar_contrato(self, dados):
        query = """INSERT INTO Contratos 
                   (funcionario_id, tipo_contrato, salario, data_inicio, data_fim, multa_rescisoria)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        return self.db.executar_comando(query, dados)

class ContratoCLT(ContratoModel):
    def calcular_multa(self, salario):
        return salario * 0.4

class ContratoPJ(ContratoModel):
    def calcular_multa(self, salario):
        return salario * 0.1

class ContratoEstagio(ContratoModel):
    def calcular_multa(self, salario):
        return 0