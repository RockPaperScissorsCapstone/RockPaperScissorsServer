from Queue import myQueue
from DataBaseManager import DBManager
from MultiplayerSession import MultiplayerSession
from Session import session
import socket

class api:

    def __init__(self, DBC):
        self.dbm = DBManager(DBC)

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
        return self.dbm.CreateAccount(userInfo)

    def UpdateAccountInfo(self, que):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        param = [userName, userID]
        return self.dbm.updateAccountInfo(param)
    
    def Login(self, que):
        userName = self.Decoded(que.removefromq())
        password = self.Decoded(que.removefromq())
        userInfo=[userName, password]
        return self.dbm.Login(userInfo)
       
    def AI_fetch(self, que):#FOR TESTING PURPOSES ONLY
        userID = self.Decoded(que.removefromq())
        pmove = self.Decoded(que.removefromq())
        presult = self.Decoded(que.removefromq())
        moveInfo = [userID, pmove, presult]
        return self.dbm.AI_fetch(moveInfo)
        
    def CreateSession(self, conn):
        apiSession = session(self.dbm) 
        return apiSession.startSession(conn)

    def UpdateWinLoss(self, que):
        wins = self.Decoded(que.removefromq())
        print("wins: ", wins)
        losses = self.Decoded(que.removefromq())
        print("losses: ", losses)
        userID = self.Decoded(que.removefromq())
        print("id: ", userID)
        param = [wins, losses, userID]
        return self.dbm.updateWinLoss(param)

    def UpdateScore(self, que):
        winnerId = self.Decoded(que.removefromq())
        winnerScore = self.Decoded(que.removefromq())
        loserId = self.Decoded(que.removefromq())
        loserScore = self.Decoded(que.removefromq())
        param = [winnerId, winnerScore, loserId, loserScore]
        return self.dbm.updateScore(param)
        
    def Leaderboard(self, que):
        return self.dbm.leaderboard()

    def Inventory(self, que):
        userId = self.Decoded(que.removefromq())
        return self.dbm.getInventory(userId)

    def Shop(self, que):
        return self.dbm.shop()
    
    def addFriend(self, que):
        username1 = self.Decoded(que.removefromq())
        username2 = self.Decoded(que.removefromq())
        twofriends = [username1, username2]
        return self.dbm.addFriend(twofriends)
    
    def findFriends(self, que):
        username = self.Decoded(que.removefromq())
        return self.dbm.findFriends(username)
    
    def addMessage(self, que, messenger, playerPackage):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        messageType = self.Decoded(que.removefromq())
        if(messageType == "Challenge Accepted"):
            success = ""
            cUserID = self.dbm.getPlayerIDFromUserName(userName)
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
                        multiplayerSession = MultiplayerSession(challenge[1], playerPackage, messenger, self.dbm)
                        multiplayerSession.start()
                    break
                success = "0"
            return(success)
        elif(messageType == "Challenge Message"):
            challengePackage = (userID, playerPackage)
            messenger.challengeMade(challengePackage)
            result = self.dbm.challenge([userID, userName, messageType])
            playerPackage[0].sendall("Finished".encode('ascii'))
            return "wait"
        else:
            result = self.dbm.challenge([userID, userName, messageType])
        return result
    
    def deleteMessage(self, que):
        userID = self.Decoded(que.removefromq())
        userName = self.Decoded(que.removefromq())
        messageType = self.Decoded(que.removefromq())
        return self.dbm.deleteMessage([userID, userName, messageType])
        
    def returnMessages(self, que):
        userName = self.Decoded(que.removefromq())
        return self.dbm.returnMessages([userName])

    def puchaseItem(self, que):
        winnerId = self.Decoded(que.removefromq())
        loserId = self.Decoded(que.removefromq())
        return self.dbm.puchaseItem(winnerId, loserId)