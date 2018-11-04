from API import api
import socket
import threading
from Queue import myQueue


class Assigner(threading.Thread):

    def __init__(self, connect):
        threading.Thread.__init__(self)
        self.conn = connect
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
            else:
                print("didn't match")
                self.conn.sendall("not a matching function")
        print("Connection Closed")

