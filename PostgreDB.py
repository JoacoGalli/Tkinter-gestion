import psycopg2

class PostgreDB():
    def __init__(self):
        self.url = 'localhost'
        self.user = 'postgres'
        self.password = 'password'
        self.database = 'Usuarios'
        self.port = '5432'
        self.connection = psycopg2.connect(host = self.url, user = self.user, password = self.password, database = self.database, port = self.port)
        self.cursor = self.connection.cursor()

    def execute(self,arg):
        try:
            self.cursor.execute(arg)
            self.consulta = self.cursor.fetchall()
        except BaseException as e:
            self.connection.rollback()

    def fetchone(self):
        return self.cursor.fetchone()
