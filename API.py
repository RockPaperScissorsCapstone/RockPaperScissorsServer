from Queue import myQueue
from DataBaseManager import DBManager
import array as arr

def class api:

    def __init__(self):
    
    
    def createAccount(que):
        userEmail =decoded(que.removefromq())
        userName = decoded(que.removefromq())
        userPassword = decoded(que.removefromq())
        userFirstName = decoded(que.removefromq())
        userLastName = decoded(que.removefromq())
        userInfo =  arr.array(userName, userEmail, userPassword, userFirstName, userLastName)
        return DBManager.CreateAccount(userInfo)
        

    def decoded(data):
        return data.decode('cp437')
                            
                                    
