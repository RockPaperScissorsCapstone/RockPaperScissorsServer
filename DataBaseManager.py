import mysql.connector
import array

class DBManager:
    cnx = None
    def __init__(self):
        try:
            cnx = mysql.connector.connect(user='DatabaseConnect', password='dbConnect',
                                  host='127.0.0.1',
                                  database='sys')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
    def CreateAccount(userInfo):
        
