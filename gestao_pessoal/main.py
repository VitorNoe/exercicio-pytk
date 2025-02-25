import tkinter as tk
from views.janelas import GerenciadorJanelas
from views.login import LoginFrame
from controllers.auth_controller import AuthController
from views.dashboards import DashboardAdmin, DashboardRH, DashboardFinanceiro
from views.contratos_view import ContratosView
from controllers.folha_controller import FolhaController

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestão de Pessoal")
        self.geometry("1024x768")
        
        # Configurações principais
        self.gerenciador_janelas = GerenciadorJanelas(self)
        self.auth_controller = AuthController(self.gerenciador_janelas)
        self.folha_controller = FolhaController()
        
        # Adicionar frames
        self.gerenciador_janelas.adicionar_frame(
            "Login", 
            lambda master: LoginFrame(master, self.auth_controller)
        )
        self.gerenciador_janelas.adicionar_frame(
            "DashboardAdmin", 
            lambda master: DashboardAdmin(master, self.auth_controller)
        )
        self.gerenciador_janelas.adicionar_frame(
            "DashboardRH", 
            lambda master: DashboardRH(master, self.auth_controller)
        )
        self.gerenciador_janelas.adicionar_frame(
            "DashboardFinanceiro", 
            lambda master: DashboardFinanceiro(master, self.auth_controller)
        )
        self.gerenciador_janelas.adicionar_frame(
            "Contratos",
            lambda master: ContratosView(master, self.contrato_controller)
        )
        
        # Frame inicial
        self.gerenciador_janelas.mostrar_frame("Login")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()