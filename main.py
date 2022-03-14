from database_connection import db_connect

name = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
base = input('Введите название  базы данных: ')
connect_one = db_connect(name, password, base)



