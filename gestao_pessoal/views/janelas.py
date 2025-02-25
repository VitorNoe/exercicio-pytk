import tkinter as tk

class GerenciadorJanelas:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        self.current_frame = None

    def adicionar_frame(self, nome, classe):
        frame = classe(self.root)
        self.frames[nome] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, nome):
        frame = self.frames.get(nome)
        if frame:
            frame.tkraise()
            self.current_frame = nome