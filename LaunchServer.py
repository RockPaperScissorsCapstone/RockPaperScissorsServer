from ConnectionManager import ConnectionManager
import threading
from RandomMatchMaker import RandomMatchMaker
from Queue import myQueue

def main():
    socketQue = myQueue()
    randomM = RandomMatchMaker(socketQue)
    cManager = ConnectionManager(socketQue)
    randomM.start()
    cManager.start()

main()