import mysql.connector


class SqlConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.database,
        )
        self.cursor = self.conn.cursor()

    def get_username(self, value):
        query = f"select Username from Students where Username = %s"

        self.cursor.execute(query, (value,))
        result = self.cursor.fetchone()
        if result == None:
            return None
        return result[0]
    
    def get_password(self, username):
        query = f"select Password from Students where Username = %s"

        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        if result == None:
            return None
        return result[0]
    
    def get_name(self, name):
        query = f"select name from Students where name = %s"
        self.cursor.execute(query, (name))
        result = self.cursor.fetchall()

        return result
    
    def update_login_date_time(self, date, time, username):
        query =  f"update Students set login_date=%s login_time=%s where Username=%s"
        self.cursor.execute(query, (date, time, username))
        return