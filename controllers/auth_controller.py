from utils.database import GerenciadorBancoDados
from models.funcionario_model import FuncionarioModel

class AuthController:
    def __init__(self, gerenciador_janelas):
        self.db = GerenciadorBancoDados()
        self.gerenciador_janelas = gerenciador_janelas
        self.usuario_logado = None

    def autenticar_usuario(self, usuario, senha):
        query = "SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s"
        result = self.db.executar_consulta(query, (usuario, senha))
        
        if result:
            self.usuario_logado = result[0]
            self.redirecionar_por_perfil()
            return True
        else:
            return False

    def redirecionar_por_perfil(self):
        perfil = self.usuario_logado['perfil']
        
        if perfil == 'admin':
            self.gerenciador_janelas.mostrar_frame("DashboardAdmin")
        elif perfil == 'rh':
            self.gerenciador_janelas.mostrar_frame("DashboardRH")
        elif perfil == 'financeiro':
            self.gerenciador_janelas.mostrar_frame("DashboardFinanceiro")

    def logout(self):
        self.usuario_logado = None
        self.gerenciador_janelas.mostrar_frame("Login")