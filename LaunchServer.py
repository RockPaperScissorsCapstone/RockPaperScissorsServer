from ConnectionManager import ConnectionManager
import threading
from RandomMatchMaker import RandomMatchMaker
from Queue import myQueue
from Messenger import Messenger
from DBConnectors import DBConnectors

def main():
    socketQue = myQueue()
    statusQue = myQueue()
    messenger = Messenger()
    DBConnections = DBConnectors()
    randomM = RandomMatchMaker(socketQue, messenger, DBConnections)
    cManager = ConnectionManager(socketQue, statusQue, messenger, DBConnections)
    randomM.start()
    cManager.start()

main()