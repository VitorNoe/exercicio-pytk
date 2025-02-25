import mysql.connector
from mysql.connector import Error

class GerenciadorBancoDados:
    def __init__(self, host='localhost', user='root', password='', database='gestao_pessoal'):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None
        self.transaction = False

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            return self.connection
        except Error as e:
            print("Erro ao conectar:", e)
            return None

    def executar_consulta(self, query, params=None):
        try:
            conn = self.conectar()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Error as e:
            print("Erro na consulta:", e)
            return []

    def executar_comando(self, query, params=None):
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute(query, params)
            if not self.transaction:
                conn.commit()
            cursor.close()
            conn.close()
            return True
        except Error as e:
            print("Erro no comando:", e)
            return False

    def iniciar_transacao(self):
        self.transaction = True
        self.conectar().start_transaction()

    def confirmar_transacao(self):
        self.connection.commit()
        self.transaction = False

    def reverter_transacao(self):
        self.connection.rollback()
        self.transaction = False