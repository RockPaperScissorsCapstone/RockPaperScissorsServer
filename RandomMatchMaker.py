from Queue import myQueue
from MultiplayerSession import MultiplayerSession
import socket
import threading
import time

class RandomMatchMaker(threading.Thread):
    socketQue = None
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.socketQue = que

    def run(self):
        print("Running RandomMatchMaker")
        while True:
            if(self.socketQue.size() > 1):
                print("Match has been made")
                playerOneAddr = self.socketQue.removefromq()
                playerTwoAddr = self.socketQue.removefromq()

                playerOne = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                playerTwo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                playerOneClientAddress = (playerOneAddr[0],65431)
                playerTwoClientAddress = (playerTwoAddr[0],65431)

                playerOne.connect(playerOneClientAddress)
                playerTwo.connect(playerTwoClientAddress)

                playerOne.sendall(("1").encode('ascii'))
                playerTwo.sendall(("1").encode('ascii'))

                playerOneConnected = playerOne.recv(1024)
                playerTwoConnected = playerTwo.recv(1024)
                
                if(playerOneConnected.decode('ascii')=="1" & playerTwoConnected.decode('ascii')=="1"):
                    multiplayerSession = MultiplayerSession(playerOne, playerTwo)
                    multiplayerSession.start()

            time.sleep(5)