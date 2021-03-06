import sqlite3


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor


db1 = Database().connect()
db2 = Database().connect()

print(f'Db 1: {db1}')
print(f'Db 2: {db2}')
