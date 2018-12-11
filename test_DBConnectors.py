import unittest
import mysql.connector
from mysql.connector import pooling
from mysql.connector import errorcode
from DBConnectors import DBConnectors
connectors = DBConnectors()
class test_DBConnectors_TestCases(unittest.TestCase):
    def test_DBConnectors_GetConnection(self):
        connectors.lockObject()
        cnx = connectors.getConnection()
        connectors.unlockObject()
        print(cnx)
    
    def test_DBConnectors_ReleaseConnection(self):
        cnx = connectors.getConnection()
        connectors.releaseConnection(cnx)

    def test_DBConnectors_GetCount(self):
        connectors.lockObject()
        print(connectors.getCount())
        connectors.unlockObject()

if __name__ == "__main__":
    unittest.main()