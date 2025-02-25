from utils.database import GerenciadorBancoDados

class UsuarioModel:
    def __init__(self):
        self.db = GerenciadorBancoDados()

    def criar_usuario(self, usuario, senha, perfil):
        query = """INSERT INTO Usuarios (usuario, senha, perfil)
                   VALUES (%s, %s, %s)"""
        return self.db.executar_comando(query, (usuario, senha, perfil))

    def autenticar(self, usuario, senha):
        query = "SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s"
        return self.db.executar_consulta(query, (usuario, senha))

    def buscar_perfil(self, usuario_id):
        query = "SELECT perfil FROM Usuarios WHERE id = %s"
        result = self.db.executar_consulta(query, (usuario_id,))
        return result[0]['perfil'] if result else None