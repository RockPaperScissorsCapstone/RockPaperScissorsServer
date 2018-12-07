from Queue import myQueue
from MultiplayerSession import MultiplayerSession
import socket
import threading
import time
from DBConnectors import DBConnectors
from DataBaseManager import DBManager

class RandomMatchMaker(threading.Thread):
    socketQue = None
    messenger = None
    def __init__(self, que, messenger, DBCP):
        threading.Thread.__init__(self)
        self.socketQue = que
        self.messenger = messenger
        self.DBCP = DBCP


    def run(self):
        print("Running RandomMatchMaker")
        while True:
            if(self.socketQue.size() > 1):
                print("Match has been made")
                dbm = DBManager(self.DBCP)
                playerOnePackage = self.socketQue.removefromq()
                playerTwoPackage = self.socketQue.removefromq()
                playerOne = playerOnePackage[0]
                playerTwo = playerTwoPackage[0]
                playerOne.sendall(("1").encode('ascii'))
                playerTwo.sendall(("1").encode('ascii'))

                playerOneConnected = playerOne.recv(1024)
                playerTwoConnected = playerTwo.recv(1024)

                if(playerOneConnected.decode('ascii')=="1" and playerTwoConnected.decode('ascii')=="1"):
                    multiplayerSession = MultiplayerSession(playerOnePackage, playerTwoPackage, self.messenger, dbm)
                    multiplayerSession.start()

            time.sleep(5)