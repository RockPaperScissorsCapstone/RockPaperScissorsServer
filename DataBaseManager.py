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
            return err

    def Login(self, userInfo):
        login = ("SELECT COUNT(*) FROM rps_user WHERE RPS_username = %s AND RPS_pass = %s")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(login, userInfo)
            result = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            if result == 1:
                return ("Login Success")
            else:
                return ("Login Failure")
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
    
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
    
    def AI_fetch(self, move_Info):
        query1 = ("SELECT COUNT(*) FROM Move_History WHERE RPS_User_id = %s, MoveH_pMove = %s, MoveH_pResult = %s, MoveH_move = Rock")
        query2 = ("SELECT COUNT(*) FROM Move_History WHERE RPS_User_id = %s, MoveH_pMove = %s, MoveH_pResult = %s, MoveH_move = Paper")
        query3 = ("SELECT COUNT(*) FROM Move_History WHERE RPS_User_id = %s, MoveH_pMove = %s, MoveH_pResult = %s, MoveH_move = Scissors")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query1, move_Info)
            result1 = cursor.fetchone()
            cursor.execute(query2, move_Info)
            result2 = cursor.fetchone()
            cursor.execute(query3, move_Info)
            result3 = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            if result1 > result2 and result1 > result3:
                return "Paper"
            elif result2 > result3 and result2 > result1:
                return "Scissors"
            else:
                return "Rock"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err