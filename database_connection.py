import sqlalchemy


class db_connect:
    def __init__(self, login, password, base):
        self.login = login
        self.password = password
        self.base = base

    def connect(self):
        db = f'postgresql://{self.login}:{self.password}@localhost:5432/{self.base}'
        engine = sqlalchemy.create_engine(db)
        connection = engine.connect()
        return connection




