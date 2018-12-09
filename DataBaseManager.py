import mysql.connector
import socket
from mysql.connector import errorcode
from mysql.connector import pooling
import array
import json
import random

class DBManager:
    cnx = None
    cnxpool = None

    def __init__(self):
        try:
            # Production Credentials
            self.cnx = mysql.connector.connect(
                user='rpsdb1',
                password='tekashi69',
                host='rpsdb1.cs0eeakwgvyu.us-east-2.rds.amazonaws.com',
                database='rpsdb1')

            self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = "rpspool",
                pool_size = 3,
                user='rpsdb1',
                password='tekashi69',
                host='rpsdb1.cs0eeakwgvyu.us-east-2.rds.amazonaws.com',
                database='rpsdb1')

            #Nick's Test Credentials
            # self.cnx = mysql.connector.connect(user='rpsNick', password='Connection',
            #                       host='rpsdb1.cs0eeakwgvyu.us-east-2.rds.amazonaws.com',
            #                       database='rpsdbTest')

            # print(self.cnx)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error: ")
                print(err)

    # Prepares and excutes the SQL statement for Create account.
    # Accepts a list of userInfo as its paramater which holds all the relavent information
    # that was sent over by the client.
    # This will insert a new row into the rps_user table with all the listed columns filled out:
    #   rps_user_username
    #   rps_user_email
    #   rps_user_password
    #   rps_user_fname
    #   rps_user_lname
    def CreateAccount(self, userInfo):
        add_user = (
            "INSERT INTO rps_user "
            "(rps_user_username, rps_user_email, rps_user_password, rps_user_fname, rps_user_lname) "
            "VALUES (%s, %s, %s, %s, %s)")
        try:
            cursor = self.cnx.cursor()
            cursor.execute(add_user, userInfo)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return("0")
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            print(str(err))
            if("username" in str(err)):
                return("1")
            elif("email" in str(err)):
                return("2")
            return str(err)

    # Prepares and executes the select statement for the login function and returns all data
    # associated with the user account with whos password and username was matched.
    # Accepts a list of params as variable userInfo which contains a username and password
    # sent over from the client
    # Returned information is:
    #   rps_user_id
    #   rps_user_username
    #   rps_user_email
    #   rps_user_fname
    #   rps_user_lname
    #   rps_user_wins
    #   rps_user_losses
    #   rps_user_currency
    #   rps_user_score
    def Login(self, userInfo):
        login = (
            "SELECT rps_user_id, rps_user_username, rps_user_email, rps_user_fname, rps_user_lname, rps_user_wins, rps_user_losses, rps_user_currency, rps_user_score FROM rps_user WHERE rps_user_username = %s AND rps_user_password = %s"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(login, userInfo)
            rows = cursor.rowcount
            #Obtains the row information in form of tuple
            result = cursor.fetchone()
            if(rows == 1):
                #Parses out the tuple into more understandable variables
                user_id = str(result[0])
                user_username = str(result[1])
                user_email = str(result[2])
                user_fname = str(result[3])
                user_lname = str(result[4])
                user_wins = str(result[5])
                user_losses = str(result[6])
                user_currency = str(result[7])
                user_score = str(result[8])
                #Packages the inforamtion into json format to be sent to client
                accountInfo_json = {
                    "user_id" : user_id, 
                    "firstname" : user_fname, 
                    "lastname" : user_lname, 
                    "email" : user_email, 
                    "username" : user_username,
                    "wins" : user_wins, 
                    "losses" : user_losses, 
                    "currency" : user_currency, 
                    "score" : user_score
                    }
                #Turns the json object into a string object
                accountInfo_string = json.dumps(accountInfo_json)

                cursor.close()
                self.cnx.close()
                return(accountInfo_string)
            else:
                cursor.close()
                self.cnx.close()
                return("Login Failure")
            # Will check to see if the login returned any information and then returns
            # said information as a string in json format
        except mysql.connector.Error as err:
            print(str(err))
            cursor.close()
            self.cnx.close()
            return str(err)
        except TypeError as err:
            print("Type Error: ")
            print(str(err))
            cursor.close()
            self.cnx.close()
            return "Invalid Username or Password"
    
    def updateAccountInfo(self, param):
        #print("param = " + param)
        get_account = (
            "UPDATE rps_user SET rps_user_username = %s WHERE rps_user_id = %s"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(get_account, param)
            #result = str(cursor.fetchone()[0])
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            #print("Returned value from db = ")
            #print(result)
            return "1"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            #print(err)
            return err

    def AI_fetch(self, move_Info):
        print(move_Info)
        query1 = ("SELECT move_history_move FROM move_history WHERE rps_user_id = %s AND move_history_pMove = %s AND move_history_pResult = %s")
        cursor = self.cnx.cursor(buffered=True)
        n = random.randrange(10,20)
        try:
            cursor.execute(query1, move_Info)
            result = cursor.fetchall()
            retval = []
            result1 = 0
            result2 = 0
            result3 = 0
            for x in result:
                retval.append(x[0])
            if len(retval) > n:
                retval = retval[len(retval)-n:len(retval)]
            for x in retval:
                if x == 1:
                    result1 += 1
                elif x == 2:
                    result2 += 1
                elif x == 3:
                    result3 += 1
            print(result1)
            print(result2)
            print(result3)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            if result1 > result2 and result1 > result3:#rock most likely
                return 2
            elif result2 > result3 and result2 > result1:#paper most likely
                return 3
            elif result3 > result2 and result3 > result1:#scissors most likely
                return 1
            elif result1 == result2 and result2 == result3:#all three equally likely, needs to be replaced with data mining when implemented
                retval = random.randrange(1, 3)
                return retval
            elif result1 == result2:#rock and paper equally likely
                return 2
            elif result2 == result3:#paper and scissors equally likely
                return 3
            elif result3 == result1:#scissors and rock equally likely
                return 1
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err

    def move_Insert(self, move_Info):
        query = (
            "INSERT into move_history (rps_user_id, move_history_pMove, move_history_pResult, move_history_move, move_history_result, move_history_round) VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query, move_Info)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return 1
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err

    def updateWinLoss(self, param):
        query = (
            "UPDATE rps_user SET rps_user_wins = %s, rps_user_losses = %s WHERE rps_user_id = %s"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query, param)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return "Updated Win and Loss!"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err

    def updateScore(self, param):
        winnerId = param[0]
        winnerScore = param[1]
        loserId = param[2]
        loserScore = param[3]
        scoreCalc = 10  #The score to be added/subtracted due to win/loss, before underdog bonus
        #Checks if there is an 'underdog' and applies score bonus accordingly
        if (loserScore - winnerScore >= 100):
            scoreCalc = scoreCalc + (winnerScore - loserScore) / 10
        query = (
            "UPDATE rps_user SET rps_user_score = %s WHERE rps_user_id = %s")
        queryInfoWinner = [winnerScore + scoreCalc, winnerId]
        queryInfoLoser = [loserScore - scoreCalc, loserId]
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query, queryInfoWinner)
            cursor.execute(query, queryInfoLoser)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return "Updated Score!"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
        finally:
            cursor.close()

    def leaderboard(self):
        query = (
            "SELECT rps_user_username, rps_user_score FROM rps_user ORDER BY rps_user_score"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query)
            #Places all rows of query into 'result'
            result = cursor.fetchall()
            return result
            #  Old code
            #self.cnx.commit()
            #cursor.close()
            #self.cnx.close()
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
        finally:
            cursor.close()

    def getInventory(self, userId):
        query = ("SELECT purchase_skin_tag FROM purchases WHERE purchase_user_id = $s")
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query, userId)
            #Places all rows of query into 'result'
            result = cursor.fetchall()
            return result
            #  Old code
            #self.cnx.commit()
            #cursor.close()
            #self.cnx.close()
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
        finally:
            cursor.close()

    def shop(self):
        query = ("SELECT skin_name, skin_tag, skin_price FROM skins ORDER BY skin_price")
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query)
            #Places all rows of query into 'result'
            result = cursor.fetchall()
            return result
            #  Old code
            #self.cnx.commit()
            #cursor.close()
            #self.cnx.close()
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
        finally:
            cursor.close()
    
    def addFriend(self, twofriends):
        query = (
            "INSERT INTO friends (player_username, player2_username) VALUES (%s, %s)"
        )
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query, twofriends)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return "1"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err

    def findFriends(self, username):
        query = (
            "SELECT player_username FROM friends WHERE player2_username = %s UNION SELECT player2_username FROM friends WHERE player_username = %s"
        )
        inHouse = []
        inHouse.append(username)
        inHouse.append(username)
        cursor = self.cnx.cursor()
        print("Entering try")
        try:
            cursor.execute(query, inHouse)
            sqlretval = cursor.fetchall()
            cursor.close()
            self.cnx.close()
            print(sqlretval)
            holdretval = ()
            for x in sqlretval:
                print(x)
                holdretval = holdretval + x
            retval = ""
            for x in holdretval:
                print(x)
                retval = retval + x
                retval = retval + ","
            print(len(retval))
            return retval
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            print(err)
            return err

    def deleteMessage(self, que):
        query1 = (
            "SELECT rps_user_ID FROM rps_user WHERE rps_user_username = %s")
        query2 = (
            "DELETE FROM messages WHERE receiver_id = %s AND sender_id = %s AND message_content = %s"
        )
        cursor = self.cnx.cursor()
        try:
            inHouse = []
            inHouse.append(que[1])
            cursor.execute(query1, inHouse)
            sqlretval = cursor.fetchone()
            print(sqlretval)
            sqlretval = sqlretval[0]
            inHouse = [que[0], sqlretval, que[2]]
            print(inHouse[1])
            cursor.execute(query2, inHouse)
            self.cnx.commit()
            self.cnx.close()
            cursor.close()
            self.cnx.close()
            return "Message Deleted"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            err = str(err._full_msg)
            print(err)
            return err

    def challenge(self, que):
        query1 = (
            "SELECT rps_user_ID FROM rps_user WHERE rps_user_username = %s")
        print(que)
        query2 = (
            "INSERT INTO messages (sender_id, receiver_id, message_content) VALUES (%s, %s, %s)"
        )
        cursor = self.cnx.cursor()
        try:
            inHouse = []
            inHouse.append(que[1])
            print(inHouse)
            cursor.execute(query1, inHouse)
            sqlretval = cursor.fetchone()
            print(sqlretval)
            sqlretval = sqlretval[0]
            inHouse = [que[0], sqlretval, que[2]]
            cursor.execute(query2, inHouse)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return "Challenge Made"
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            err = str(err)
            print(err)
            return err

    def returnMessages(self, que):
        query1 = ("SELECT sender_id, message_content FROM messages WHERE receiver_id = %s")
        query2 = ("SELECT rps_user_username FROM rps_user WHERE rps_user_ID IN (%s)")
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query1, que)
            sqlretval = cursor.fetchall()
            inHouse = []
            for x in sqlretval:
                inHouse.append(x[0])
            print(inHouse)
            in_p = ", ".join(map(lambda x: "%s", inHouse))
            query2 = query2 % in_p
            cursor.execute(query2, inHouse)
            sqlretval2 = cursor.fetchall()
            retval = ""
            counter = 0
            while counter < len(sqlretval2):
                retval += sqlretval2[counter][0]
                retval += ","
                retval += sqlretval[counter][1]
                retval += ","
                counter += 1
            cursor.close()
            self.cnx.close()
            print(retval)
            return retval
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            err = str(err)
            print(err)
            return err
        return 0

    def getPlayerIDFromUserName(self, param):
        print("We are in get player id")
        print(param)
        query = ("SELECT rps_user_ID FROM rps_user WHERE rps_user_username = %s")
        cursor = self.cnx.cursor()
        try:
            userName = [param, ]
            cursor.execute(query, userName)
            retval = cursor.fetchone()
            cursor.close()
            self.cnx.close()
            print(retval[0])
            return str(retval[0])
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            err = str(err)
            print(err)
            return err
    def autoMoveRemover(self):
        query = "DELETE FROM move_history WHERE rps_user_id = 19"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(query)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
        return 0
    def getUserScore(self, userid):
        query = ("SELECT rps_user_score FROM rps_user WHERE rps_user_userid = %s", userid)
        cursor = self.cnx.cursor(buffered=True)
        try:
            print("getUserScore executing")
            cursor.execute(query)
            sqlretval = cursor.fetchall()
            cursor.close()
            self.cnx.close()
            print(str(sqlretval[0]))
            return str(sqlretval[0])
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err
    
    def updateCurrency(self, buf):
        winnerScoreQuery = ("SELECT rps_user_score FROM rps_user WHERE rps_user_id = %s")
        loserScoreQuery = ("SELECT rps_user_score FROM rps_user WHERE rps_user_id = %s")
        cnx1 = self.cnxpool.get_connection()
        # cursor = self.cnx.cursor(buffered=True)
        cursor = cnx1.cursor(buffered=True)
        try:
            print("updateCurrency executing")
            print("buf[0]: ", buf[0])
            buf0 = (buf[0], )
            cursor.execute(winnerScoreQuery, buf0)
            print("winnerScoreQuery executed")

            print("winnerScoreQuery cursor fetch start")
            winnerScore = cursor.fetchall()
            print("winnerScoreQuery cursor fetch end")
            winnerScore = winnerScore[0]
            buf1 = (buf[1], )
            cursor.execute(loserScoreQuery, buf1)
            loserScore = cursor.fetchall()
            loserScore = loserScore[0]

            print("Winner Score: ", str(winnerScore))
            print("Loser Score: ", str(loserScore))

            scoreDiff = abs(winnerScore[0] - loserScore[0])
            print("Score difference: ", scoreDiff)

            # score diff 100 and winner has less score. underdog win
            if scoreDiff >= 100 and loserScore > winnerScore:
                underdogUpdateCurrencyQuery = ("UPDATE rps_user SET rps_user_currency = rps_user_currency + 15 WHERE rps_user_id = %s")
                cursor.execute(underdogUpdateCurrencyQuery, buf0)
                # self.cnx.commit()
                cnx1.commit()
                # print("Updated Currency (Underdog) for userid: ", winnerid)
            else:
                regularUpdateCurrencyQuery = ("UPDATE rps_user SET rps_user_currency = rps_user_currency + 10 WHERE rps_user_id = %s")
                cursor.execute(regularUpdateCurrencyQuery, buf0)
                # self.cnx.commit()
                cnx1.commit()
                # print("Updated Currency for userid: ", winnerid)
            
            #return updated currency to winner
            getCurrencyQuery = ("SELECT rps_user_currency FROM rps_user WHERE rps_user_id = %s")
            cursor.execute(getCurrencyQuery, buf0)
            updatedCurrency = cursor.fetchall()
            print("Updated Currency: ", str(updatedCurrency[0]))
            cursor.close()
            cnx1.close()
            return str(updatedCurrency[0][0])
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err

    # def updateCurrency(self, userid, gain):
    #     query = ("UPDATE rps_user SET rps_user_currency = rps_user_currency + %s WHERE rps_user_userid = %s", (gain, userid))
    #     cursor = self.cnx.cursor(buffered=True)
    #     try:
    #         cursor.execute(query)
    #         result = cursor.fetchall()
    #         cursor.close()
    #         self.cnx.close()
    #         return "Updated Currency!"
    #     except mysql.connector.Error as err:
    #         cursor.close()
    #         self.cnx.close()
    #         return err
    
    def getCurrency(self, userid):
        query = ("SELECT rps_user_currency FROM rps_user WHERE rps_user_userid = %s", userid)
        cursor = self.cnx.cursor(buffered=True)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            self.cnx.close()
            print("updated currency: ", result[0])
            return str(result[0])
        except mysql.connector.Error as err:
            cursor.close()
            self.cnx.close()
            return err