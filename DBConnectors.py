import mysql.connector
from mysql.connector import pooling
from mysql.connector import errorcode
import array
import threading

class DBConnectors:
    cnxpool = None
    lock = threading.RLock()
    def __init__(self):
        try:
            pooling.CNX_POOL_MAXSIZE = 40
            self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name = "rpspool",
                    pool_size = 40,
                    pool_reset_session= True,
                    user='rpsdb1',
                    password='tekashi69',
                    host='rpsdb1.cs0eeakwgvyu.us-east-2.rds.amazonaws.com',
                    database='rpsdb1')
            self.availableConnections = 32
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error: ")
                print(err)

    def releaseConnection(self, connection):
        # self.cnxpool.add_connection(connection)
        connection.close()
        with self.lock:
            print("got lock increasing availableConnections by 1")
            self.availableConnections += 1

    def getConnection(self):
        print("got lock reducing availableConnections by 1")
        self.availableConnections -= 1 
        return self.cnxpool.get_connection()

    def getCount(self):
        print("Got lock and returning the number of available connections")
        return self.availableConnections

    def lockObject(self):
        self.lock.acquire()

    def unlockObject(self):
        self.lock.release()