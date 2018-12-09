from API import api
import socket
import threading
from Queue import myQueue
from Messenger import Messenger
import time


class Assigner(threading.Thread):

    def __init__(self, connect, socketQue, addr, messages):
        threading.Thread.__init__(self)
        self.conn = connect
        self.socketQue = socketQue
        self.addr = addr
        self.messages = messages
        #run = threading.Thread(target=self,args=())
        print("Started thread")
        #run.start()

    def run(self):
        print("started run")
        myQue = myQueue()
        result = None
        function = None
        with self.conn:
            #print('Connected by', addr)
            # Collects all data that has been sent and stores it in a
            # first in first out que and ends when the "end" message is sent
            # over from the client
            while True:
                data = self.conn.recv(1024)
                if data.decode('ascii') == "end":
                    break
                myQue.addtoq(data)
                print(data.decode('ascii'))
                self.conn.sendall(data)
            function = (myQue.removefromq()).decode('ascii')
            print("function = " + function)
            print("reached")
            # Starts the Create Account Process
            if(function == "CreateAccount"):
                APICommand = api()
                result = APICommand.CreateAccount(myQue)
                print("result: " + result)
                self.conn.sendall(result.encode(encoding='ascii'))
            # Starts the update Account process NEEDS TO BE REDONE OLD FUNCTION IS DEPRICATED
            elif(function == "UpdateAccountInfo"):
                APICommand = api()
                result = APICommand.UpdateAccountInfo(myQue)
                print("result: " + result)
                self.conn.sendall(result.encode('ascii'))
            # Starts the login process
            elif(function == "Login"):
                if myQue[1] in self.statusQue:
                    self.conn.send("Login Failed".encode('ascii'))
                    return
                APIcommand = api()
                result = APIcommand.Login(myQue)
                print("result: " + result)
                self.conn.send(result.encode(encoding='ascii'))
            # Starts game with AI
            elif(function == "AIGame"):
                APICommand = api()
                result = APICommand.AI_fetch(myQue)
                print("result: " + result)
                self.conn.sendall(str(result).encode(encoding='ascii'))
            # Starts session
            elif(function == "Session"):
                APICommand = api()
                result = APICommand.CreateSession(self.conn)
                self.conn.sendall(result.encode(encoding='ascii'))
            elif(function == "UpdateWinLoss"):
                APICommand = api()
                result = APICommand.UpdateWinLoss(myQue)
                print("result: " + result)
                self.conn.sendall(result.encode('ascii'))
            # Updates winner and loser scores
            elif(function == "UpdateScore"):
                APICommand = api()
                result = APICommand.UpdateScore(myQue)
                print("result: " + result)
                self.conn.sendall(result.encode('ascii'))
            # Retrieves leaderbord data
            elif(function == "Leaderboard"):
                APICommand = api()
                result = APICommand.Leaderboard(myQue)
                resultString = ""
                for x in range(len(result)):
                    resultString += result[x][0]
                    resultString += ","+ str(result[x][1])
                    resultString += ";"
                print(resultString)
                self.conn.sendall(resultString.encode('ascii'))
            elif(function == "PlayWithRandom"):
                package = (self.conn, self.addr)
                self.socketQue.addtoq(package)
                while True:
                    messageList = self.messages.getList()
                    if self.addr[0] in messageList:
                        self.messages.removeFromList(self.addr[0])
                        break
                    else:
                        time.sleep(1)
            elif(function == "addMessage"):
                APICommand = api()
                result = APICommand.addMessage(myQue)
                self.conn.sendall(result.encode('ascii'))
            elif(function == "returnMessages"):
                APICommand = api()
                result = APICommand.returnMessages(myQue)
                self.conn.sendall(result.encode('ascii'))
            elif(function == "addFriend"):
                APICommand = api()
                result = APICommand.addFriend(myQue)
                self.conn.sendall(str(result).encode('ascii'))
            elif(function == "findFriends"):
                APICommand = api()
                result = APICommand.findFriends(myQue)
                self.conn.sendall(result.encode('ascii'))
            else:
                print("didn't match")
                self.conn.sendall("not a matching function")
        print("Connection Closed")

