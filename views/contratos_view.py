import tkinter as tk
from tkinter import ttk
from views.formularios import FormularioBase
from controllers.contrato_controller import ContratoController
from models.funcionario_model import FuncionarioModel

class ContratosView(FormularioBase):
    def __init__(self, master, controller):
        campos = [
            {"label": "Funcionário", "tipo": "combobox", "opcoes": self.carregar_funcionarios},
            {"label": "Tipo Contrato", "tipo": "combobox", "opcoes": ["CLT", "PJ", "Estágio"]},
            {"label": "Salário", "tipo": "entry", "validacao": "decimal"},
            {"label": "Data Início", "tipo": "date"},
            {"label": "Data Fim", "tipo": "date"},
            {"label": "Multa Rescisória", "tipo": "entry", "estado": "readonly"}
        ]
        
        super().__init__(master, campos)
        self.controller = controller
        self.btn_calcular = ttk.Button(self, text="Calcular Multa", command=self.calcular_multa)
        self.btn_calcular.grid(row=len(campos)+1, columnspan=2)

    def carregar_funcionarios(self):
        funcionarios = FuncionarioModel().listar_ativos()
        return [f"{f['id']} - {f['nome']}" for f in funcionarios]

    def calcular_multa(self):
        tipo = self.obter_valor("Tipo Contrato")
        salario = float(self.obter_valor("Salário"))
        multa = self.controller.calcular_multa(tipo, salario)
        self.definir_valor("Multa Rescisória", f"R$ {multa:.2f}")

    def validar(self):
        # Implementar validação de datas e campos
        dados = {
            'funcionario_id': int(self.obter_valor("Funcionário").split(" - ")[0]),
            'tipo': self.obter_valor("Tipo Contrato"),
            'salario': float(self.obter_valor("Salário")),
            'data_inicio': self.obter_valor("Data Início"),
            'data_fim': self.obter_valor("Data Fim"),
            'multa': float(self.obter_valor("Multa Rescisória").replace("R$ ", ""))
        }
        
        if self.controller.salvar_contrato(dados):
            print("Contrato salvo com sucesso!")