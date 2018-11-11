from Queue import myQueue
from MultiplayerSession import MultiplayerSession
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
                playerOne = self.socketQue.removefromq()
                playerTwo = self.socketQue.removefromq()
                multiplayerSession = MultiplayerSession(playerOne, playerTwo)
                multiplayerSession.start()

            time.sleep(5)