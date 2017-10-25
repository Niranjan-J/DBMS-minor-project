from ORM.dbconnect import Connector

class User():

    def __init__(self):
        self.con = Connector()

    def createTable(self):
        self.con.create("""
            CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER AUTO_INCREMENT,
            username VARCHAR(50) NOT NULL ,
            email VARCHAR(50) NOT NULL ,
            password VARCHAR(200) NOT NULL ,

            PRIMARY KEY (user_id),
            UNIQUE (username, email, password)
            );
            """)

    def createUser(self,data):
        self.con.modify("""
            INSERT INTO User(email,username,password) VALUES (%s,%s,%s)
            """,data['email'],data['username'],data['password']
            )
