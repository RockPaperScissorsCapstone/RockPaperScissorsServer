import unittest
import mysql.connector
from mysql.connector import pooling
from mysql.connector import errorcode
from DBConnectors import DBConnectors
from DataBaseManager import DBManager
connectors = DBConnectors()
DBM = DBManager(connectors)

class test_DataBaseManager_TestCases(unittest.TestCase):
    def test_DataBaseManager_CreateAccount(self):
        param = ("TestUser123", "This@Email.Com", "Free", "FRee", "Bird")
        result = DBM.CreateAccount(param)
        print(result)
    
    def test_DataBaseManager_Login(self):
        param = ("Fresh", "test")
        result = DBM.Login(param)
        print(result)

    def test_DataBaseManager_updateAccountInfo(self):
        param = ("TestUser123", )
        user_id = DBM.getPlayerIDFromUserName(param)
        param2 = ("WinderWind", user_id)
        result = DBM.updateAccountInfo(param2)
        print(result)

    def test_DataBaseManager_AI_fecth(self):
        param = ("Fresh", "1", "1")
        result = DBM.AI_fetch(param)
        print(result)

    def test_DataBaseManager_updateWinLoss(self):
       param = ("500", "2", "30")
       result = DBM.updateWinLoss(param)
       print(result)

    def test_DataBseManager_getScore(self):
        param = ("30", )
        result = DBM.getScore(param)
        print(result)

    def test_DataBaseManager_updateScore(self):
        param = ("500", "30")
        result = DBM.updateScore(param)
        param2 = ("30", )
        print(DBM.getScore(param2))

    def test_DataBaseManager_leaderboard(self):
        result = DBM.leaderboard()
        print(result)

    def test_DataBaseManager_getInventory(self):
        param = ("30", )
        result = DBM.getInventory(param)
        print(result)

    def test_DataBaseManager_shop(self):
        result = DBM.shop()
        print(result)

    def test_DataBaseManager_findFriends(self):
        param = ("Fresh", )
        result = DBM.findFriends(param)
        print(result)

    def test_DataBaseManager_getPlayerIDFromUserName(self):
        param = ("Fresh", )
        result = DBM.getPlayerIDFromUserName(param)
        print(result)

    def test_DataBaseManager_getUsernameFromPlayerID(self):
        param = ("30", )
        result = DBM.getUsernameFromPlayerID(param)
        print(result)

    def test_DataBaseManager_getUserScore(self):
        param = ("30", )
        result = DBM.getUserScore(param)
        print(result)

    def test_DataBaseManager_getCurrnecy(self):
        param = "30"
        result = DBM.getCurrency(param)
        print(result)

    def test_DataBaseManager_setPlayerCurrency(self):
        param = ("500", "30")
        result = DBM.setPlayerCurrency(param)
        print(result)

if __name__ == "__main__":
    unittest.main()