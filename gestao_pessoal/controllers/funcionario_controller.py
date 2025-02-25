from models.funcionario_model import FuncionarioModel
from views.formularios import FormularioBase

class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()
        self.view = None

    def configurar_view(self, view):
        self.view = view

    def salvar_funcionario(self, dados):
        try:
            if self.model.criar_funcionario(dados):
                print("Funcionário salvo!")
        except Exception as e:
            print("Erro:", e)