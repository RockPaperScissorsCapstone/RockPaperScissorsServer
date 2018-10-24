from Queue import myQueue
from DataBaseManager import DBManager
from Session import StartSession
import socket

class api:

    def __init__(self):
        hi = "hi"
    
    def Decoded(self, data):
        result = data.decode('cp437')
        return result

    def CreateAccount(self, que):
        userName = self.Decoded(que.removefromq())
        userEmail = self.Decoded(que.removefromq())
        userFirstName = self.Decoded(que.removefromq())
        userLastName = self.Decoded(que.removefromq())
        userPassword = self.Decoded(que.removefromq())
        userInfo = [userName, userEmail, userPassword, userFirstName, userLastName]
        dbm = DBManager()
        return dbm.CreateAccount(userInfo)

    def CreateSession(conn):
        session = Session() 
        return session.StartSession(conn)
        
        
                            
                                    
