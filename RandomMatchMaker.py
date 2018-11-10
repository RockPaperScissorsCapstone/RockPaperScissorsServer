from Queue import myQueue
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
                #launch multiplayer session passing in both sockets
            time.sleep(5)