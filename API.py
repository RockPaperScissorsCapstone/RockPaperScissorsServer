from Queue import myQueue
from DataBaseManager import DBManager
from MultiplayerSession import MultiplayerSession
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
        print("username = " + userName)
        userEmail = self.Decoded(que.removefromq())
        print("email = " + userEmail)
        userFirstName = self.Decoded(que.removefromq())
        print("firstname = " + userFirstName)
        userLastName = self.Decoded(que.removefromq())
        print("lastname = " + userLastName)
        userPassword = self.Decoded(que.removefromq())
        print("password = " + userPassword)
        userInfo = [userName, userEmail, userPassword, userFirstName, userLastName]
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
        userInfo=[userName, password]
        dbm = DBManager()
        return dbm.Login(userInfo)
       
    def AI_fetch(self, que):#FOR TESTING PURPOSES ONLY
        userID = self.Decoded(que.removefromq())
        pmove = self.Decoded(que.removefromq())
        presult = self.Decoded(que.removefromq())
        moveInfo = [userID, pmove, presult]
        dbm = DBManager()
        return dbm.AI_fetch(moveInfo)
        
    def CreateSession(self, conn):
        apiSession = session() 
        return apiSession.startSession(conn)

    def UpdateWinLoss(self, que):
        wins = self.Decoded(que.removefromq())
        losses = self.Decoded(que.removefromq())
        userID = self.Decoded(que.removefromq())
        dbm = DBManager()
        param = [wins, losses, userID]
        return dbm.updateWinLoss(param)

    def UpdateScore(self, que):
        winnerId = self.Decoded(que.removefromq())
        winnerScore = self.Decoded(que.removefromq())
        loserId = self.Decoded(que.removefromq())
        loserScore = self.Decoded(que.removefromq())
        dbm = DBManager()
        param = [winnerId, winnerScore, loserId, loserScore]
        return dbm.updateScore(param)
        
    def Leaderboard(self, que):
        dbm = DBManager()
        return dbm.leaderboard()

    def Inventory(self, que):
        userId = self.Decoded(que.removefromq())
        dbm = DBManager()
        return dbm.getInventory(userId)

    def Shop(self, que):
        dbm = DBManager()
        return dbm.shop()
    
    def addFriend(self, que):
        username1 = self.Decoded(que.removefromq())
        username2 = self.Decoded(que.removefromq())
        twofriends = [username1, username2]
        dbm = DBManager()
        return dbm.addFriend(twofriends)
    
    def findFriends(self, que):
        username = self.Decoded(que.removefromq())
        dbm = DBManager()
        return dbm.findFriends(username)
    
    def addMessage(self, que, messenger, playerPackage):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        messageType = self.Decoded(que.removefromq())
        dbm = DBManager()
        if(messageType == "Challenge Accepted"):
            success = ""
            cUserID = dbm.getPlayerIDFromUserName(userName)
            challenges = messenger.getChallengeList()
            for challenge in challenges:
                if(challenge[0] == cUserID):
                    success = "wait"
                    playerOne = challenge[1][0]
                    playerTwo = playerPackage[0]
                    playerOne.sendall(("1").encode('ascii'))
                    playerTwo.sendall(("Finished").encode('ascii'))
                    playerTwo.sendall(("1").encode('ascii'))

                    playerOneConnected = playerOne.recv(1024)
                    playerTwoConnected = playerTwo.recv(1024)

                    if(playerOneConnected.decode('ascii')=="1" and playerTwoConnected.decode('ascii')=="1"):
                        multiplayerSession = MultiplayerSession(challenge[1], playerPackage, messenger)
                        multiplayerSession.start()
                    break
                success = "0"
            return(success)
        elif(messageType == "Challenge Message"):
            challengePackage = (userID, playerPackage)
            messenger.challengeMade(challengePackage)
            result = dbm.challenge([userID, userName, messageType])
            playerPackage[0].sendall("Finished".encode('ascii'))
            return "wait"
        else:
            result = dbm.challenge([userID, userName, messageType])
        return result
    
    def deleteMessage(self, que):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        messageType = self.Decoded(que.removefromq())
        dbm = DBManager()
        return dbm.deleteMessage([userID, userName, messageType])
        
    def returnMessages(self, que):
        userName = self.Decoded(que.removefromq())
        dbm = DBManager()
        return dbm.returnMessages([userName])