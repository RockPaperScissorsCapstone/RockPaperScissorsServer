import mysql.connector
from mysql.connector import pooling
from mysql.connector import errorcode
import array

class DBConnectors:
    cnxpool = None

    def __init__(self):
        try:
            self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name = "rpspool",
                    pool_size = 32,
                    user='rpsdb1',
                    password='tekashi69',
                    host='rpsdb1.cs0eeakwgvyu.us-east-2.rds.amazonaws.com',
                    database='rpsdb1')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error: ")
                print(err)

    def releaseConenction(self, connection):
        connection.close()
        self.cnxpool.add_connection()

    def getConnection(self):
        return self.cnxpool.get_connection()