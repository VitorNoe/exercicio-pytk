import tkinter as tk
from tkinter import ttk

class BaseDashboard(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_header()
        self.create_content()

    def create_header(self):
        header = tk.Frame(self, bg="#2c3e50")
        header.pack(fill="x", padx=10, pady=5)
        
        tk.Label(header, text="Sistema de Gestão de Pessoal", 
                fg="white", bg="#2c3e50", font=('Arial', 14)).pack(side="left")
        
        tk.Button(header, text="Sair", command=self.controller.logout,
                 bg="#e74c3c", fg="white").pack(side="right", padx=10)

    def create_content(self):
        # Método abstrato para ser implementado nas subclasses
        raise NotImplementedError

class DashboardAdmin(BaseDashboard):
    def create_content(self):
        content = tk.Frame(self)
        content.pack(pady=20)
        
        botoes = [
            ("Gerenciar Usuários", self.abrir_usuarios),
            ("Relatórios", self.abrir_relatorios),
            ("Todos os Funcionários", self.abrir_funcionarios)
        ]
        
        for texto, comando in botoes:
            tk.Button(content, text=texto, width=20, 
                     command=comando).pack(pady=5)

    def abrir_usuarios(self):
        self.controller.gerenciador_janelas.mostrar_frame("Usuarios")

class DashboardRH(BaseDashboard):
    def create_content(self):
        content = tk.Frame(self)
        content.pack(pady=20)
        
        botoes = [
            ("Cadastrar Funcionário", self.abrir_cadastro),
            ("Contratos", self.abrir_contratos),
            ("Folha de Pagamento", self.abrir_folha)
        ]
        
        for texto, comando in botoes:
            tk.Button(content, text=texto, width=20, 
                     command=comando).pack(pady=5)

class DashboardFinanceiro(BaseDashboard):
    def create_content(self):
        content = tk.Frame(self)
        content.pack(pady=20)
        
        botoes = [
            ("Folha de Pagamento", self.abrir_folha),
            ("Relatórios Financeiros", self.abrir_relatorios)
        ]
        
        for texto, comando in botoes:
            tk.Button(content, text=texto, width=20, 
                     command=comando).pack(pady=5)