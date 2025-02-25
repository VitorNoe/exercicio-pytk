from models.contrato_model import ContratoCLT, ContratoPJ, ContratoEstagio
from utils.database import GerenciadorBancoDados

class ContratoController:
    def __init__(self):
        self.db = GerenciadorBancoDados()
        self.tipos_contrato = {
            'CLT': ContratoCLT(),
            'PJ': ContratoPJ(),
            'Estágio': ContratoEstagio()
        }

    def criar_contrato(self, funcionario_id, tipo, salario, datas):
        contrato = self.tipos_contrato.get(tipo)
        if not contrato:
            return False
            
        multa = contrato.calcular_multa(salario)
        dados = (
            funcionario_id,
            tipo,
            salario,
            datas['inicio'],
            datas['fim'],
            multa
        )
        
        return contrato.criar_contrato(dados)

    def validar_datas(self, inicio, fim):
        return inicio < fim if inicio and fim else False

    def buscar_contratos_ativos(self):
        query = """SELECT c.*, f.nome 
                   FROM Contratos c
                   JOIN Funcionarios f ON c.funcionario_id = f.id
                   WHERE c.data_fim > CURDATE()"""
        return self.db.executar_consulta(query)