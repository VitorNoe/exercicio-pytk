from utils.database import GerenciadorBancoDados
from models.contrato_model import ContratoCLT, ContratoPJ, ContratoEstagio

class FolhaController:
    def __init__(self):
        self.db = GerenciadorBancoDados()
        self.calculadora = CalculadoraFolha()

    def calcular_folha(self, funcionario_id, mes_ano, horas, descontos=0, beneficios=0):
        contrato = self.obter_contrato_valido(funcionario_id)
        if not contrato:
            return None

        bruto = self.calculadora.calcular_bruto(
            contrato['tipo_contrato'],
            contrato['salario'],
            horas
        )
        
        liquido = self.calculadora.calcular_liquido(bruto, descontos, beneficios)
        
        return {
            'bruto': bruto,
            'liquido': liquido,
            'descontos': descontos,
            'beneficios': beneficios
        }

    def salvar_folha(self, dados):
        query = """INSERT INTO Folha_Pagamento 
                   (funcionario_id, mes_ano, horas_trabalhadas, valor_pago, descontos, beneficios)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (
            dados['funcionario_id'],
            dados['mes_ano'],
            dados['horas'],
            dados['liquido'],
            dados['descontos'],
            dados['beneficios']
        )
        return self.db.executar_comando(query, params)

    def obter_contrato_valido(self, funcionario_id):
        query = """SELECT * FROM Contratos 
                   WHERE funcionario_id = %s 
                   AND CURDATE() BETWEEN data_inicio AND data_fim"""
        return self.db.executar_consulta(query, (funcionario_id,))

class CalculadoraFolha:
    @staticmethod
    def calcular_bruto(tipo_contrato, salario_base, horas):
        if tipo_contrato == 'CLT':
            return salario_base + (horas * (salario_base / 220))
        elif tipo_contrato == 'PJ':
            return salario_base
        elif tipo_contrato == 'Estágio':
            return salario_base * 0.8

    @staticmethod
    def calcular_liquido(bruto, descontos, beneficios):
        return bruto - descontos + beneficios