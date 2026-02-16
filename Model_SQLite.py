import sqlite3
from hashlib import sha256

class Datas() :

    def __init__(self) :
        self.conexao = sqlite3.connect("localDatas.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS login_datas (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            user TEXT NOT NULL CHECK(length(user) <= 50),
                            email TEXT NOT NULL UNIQUE CHECK(length(email) <= 50),
                            password TEXT NOT NULL 
                            )""")
        print("Connection done")

    def Create_DataBase(self) :
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS login_datas (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            user TEXT NOT NULL CHECK(length(user) <= 50),
                            email TEXT NOT NULL UNIQUE CHECK(length(email) <= 50),
                            password TEXT NOT NULL UNIQUE
                            )""")
        self.conexao.commit()

    def delete_table(self) :
        self.cursor.execute("DROP TABLE login_datas")
        self.conexao.commit()

    def delete_user(self, user_email) :
        self.cursor.execute("DELETE FROM login_datas WHERE email = '"+ user_email +"'")
        self.conexao.commit()

    def register(self, user, email, password) :
        codefi_password = sha256(password.encode()).hexdigest()
        try : 
            self.cursor.execute("""INSERT INTO login_datas 
                            (user, email, password)
                            VALUES (?, ?, ?)""", (user, email, codefi_password))
            self.conexao.commit()
        except sqlite3.IntegrityError as e :
            print(f"Erro: {e}")

    def login_user(self, user_name, user_email, user_password) :

        #senha em sha256 recebido
        codefi_login_password = sha256(user_password.encode()).hexdigest()

        self.cursor.execute("SELECT user, password FROM login_datas WHERE email = '"+ user_email +"'")
        accounts = self.cursor.fetchall()
        for account in accounts :
            user, password = account

        #variavel password = senha em sha256 já armazenado na tabela/arquivo.db

        if (user == user_name) :
            if (codefi_login_password == password) :
                print("successfully logged")
            else :
                print("Erro : login não concluido, tente novamente")
        else :
            print("Erro: login não concluido, tente novamente")

    
open_Datas = Datas() 
 
