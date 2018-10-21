import mysql.connector
import socket
from mysql.connector import errorcode
import array

class DBManager:
    cnx = ''
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='DatabaseConnect', password='dbConnect',
                                  host='127.0.0.1',
                                  database='sys')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
    def CreateAccount(self, userInfo):
        add_user = ("INSERT INTO rps_user "
                "(RPS_username, RPS_email, RPS_pass, RPS_fName, RPS_lName) "
                "VALUES (%s, %s, %s, %s, %s)")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(add_user, userInfo)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return("User added successfully")
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return("unable to add user")

    def getAccountInfo(self, param):
        print("param = " + param)
        get_account = ("SELECT RPS_username FROM sys.rps_user WHERE RPS_User_id = %s")
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(get_account, (param,))
            result = str(cursor.fetchone()[0])
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            #print("Returned value from db = ")
            #print(result)
            return result
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            #print(err)
            return err