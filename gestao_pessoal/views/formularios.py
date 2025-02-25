import tkinter as tk
from abc import ABC, abstractmethod

class FormularioBase(tk.Frame, ABC):
    def __init__(self, master, campos):
        super().__init__(master)
        self.campos = []
        self.widgets = {}

        for idx, campo in enumerate(campos):
            label = tk.Label(self, text=campo['label'])
            label.grid(row=idx, column=0, padx=5, pady=5)
            
            if campo['tipo'] == 'entry':
                widget = tk.Entry(self)
            elif campo['tipo'] == 'combobox':
                widget = ttk.Combobox(self, values=campo['opcoes'])
            
            widget.grid(row=idx, column=1, padx=5, pady=5)
            self.widgets[campo['label']] = widget

        btn_submit = tk.Button(self, text="Salvar", command=self.validar)
        btn_submit.grid(row=len(campos), columnspan=2)

    @abstractmethod
    def validar(self):
        pass