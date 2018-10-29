from Queue import myQueue
from DataBaseManager import DBManager
from Session import session
import socket


class api:

    def __init__(self):
        hi = "hello"

    def Decoded(self, data):
        print(data)
        result = data.decode('cp437')
        print(result)
        return result

    def CreateAccount(self, que):
        userName = self.Decoded(que.removefromq())
        userEmail = self.Decoded(que.removefromq())
        userFirstName = self.Decoded(que.removefromq())
        userLastName = self.Decoded(que.removefromq())
        userPassword = self.Decoded(que.removefromq())
        userInfo = [
            userName,
            userEmail,
            userPassword,
            userFirstName,
            userLastName]
        dbm = DBManager()
        return dbm.CreateAccount(userInfo)

    def UpdateAccountInfo(self, que):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        dbm = DBManager()
        param = [userName, userID]
        return dbm.updateAccountInfo(param)
    
    def Login(self, que):
        userName = self.Decoded(que.removefromq())
        password = self.Decoded(que.removefromq())
        userInfo = [userName, password]
        dbm = DBManager()
        return dbm.Login(userInfo)

    def AI_fetch(self, que):
        userID = self.Decoded(que.removefromq())
        pmove = self.Decoded(que.removefromq())
        presult = self.Decoded(que.removefromq())
        moveInfo = [userID, pmove, presult]
        dbm = DBManager()
        return dbm.AI_fetch(moveInfo)
        
    def CreateSession(self, conn):
        apiSession = session() 
        return apiSession.startSession(conn)
        
        
                            
                                    
