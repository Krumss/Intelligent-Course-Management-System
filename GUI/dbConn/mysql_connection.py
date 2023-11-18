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
