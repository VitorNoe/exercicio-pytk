import tkinter as tk
from tkinter import ttk
from views.formularios import FormularioBase

class LoginFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        
        self.label_usuario = tk.Label(self, text="Usuário:")
        self.entry_usuario = tk.Entry(self)
        
        self.label_senha = tk.Label(self, text="Senha:")
        self.entry_senha = tk.Entry(self, show="*")
        
        self.btn_login = tk.Button(self, text="Login", command=self.autenticar)
        
        # Layout
        self.label_usuario.grid(row=0, column=0, padx=10, pady=5)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=5)
        self.label_senha.grid(row=1, column=0, padx=10, pady=5)
        self.entry_senha.grid(row=1, column=1, padx=10, pady=5)
        self.btn_login.grid(row=2, columnspan=2, pady=10)

    def autenticar(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        self.controller.autenticar_usuario(usuario, senha)