from ConnectionManager import ConnectionManager
import threading
from RandomMatchMaker import RandomMatchMaker
from Queue import myQueue
from Messenger import Messenger

def main():
    socketQue = myQueue()
    messenger = Messenger()
    randomM = RandomMatchMaker(socketQue, messenger)
    cManager = ConnectionManager(socketQue, messenger)
    randomM.start()
    cManager.start()

main()