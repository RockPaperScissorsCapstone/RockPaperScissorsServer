import socket
from Queue import myQueue
from API import api

# Production Host
# HOST = '172.31.47.99'

# Nicks Test Host
HOST = '172.31.20.135'
PORT= 65432
def main():
    print("server is up")
    while True:
        # Runs while there is data being sent over the socket.
        # can be picked up again at any time until the socket is released/closed.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # s is the socket object
            # it is being given the host and port to create an endpoint 
            # on the local system with which to listen to
            s.bind((HOST, PORT))
            s.listen()

            # When connection is established create a que with which to store the messages in.
            conn, addr = s.accept()
            myQue = myQueue()
            result = None
            function = None
            with conn:
                print('Connected by', addr)
                # Collects all data that has been sent and stores it in a
                # first in first out que and ends when the "end" message is sent
                # over from the client 
                while True:
                    data = conn.recv(1024)
                    if data.decode('ascii') == "end":
                        break
                    myQue.addtoq(data)
                    print(data.decode('ascii'))
                    conn.sendall(data)
                function = (myQue.removefromq()).decode('ascii')
                print("function = " + function)
                print("reached")
                # Starts the Create Account Process
                if(function == "CreateAccount"):
                    APICommand = api()
                    result = APICommand.CreateAccount(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode(encoding='ascii'))
                # Starts the update Account process NEEDS TO BE REDONE OLD FUNCTION IS DEPRICATED
                elif(function == "UpdateAccountInfo"):
                    APICommand = api()
                    result = APICommand.UpdateAccountInfo(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode('ascii'))
                # Starts the login process
                elif(function == "Login"):
                    APIcommand = api()
                    result = APIcommand.Login(myQue)
                    print("result: " + result)
                    conn.send(result.encode(encoding='ascii'))
                # Starts game with AI
                elif(function == "AIGame"):
                    APICommand = api()
                    result = APICommand.AI_fetch(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode(encoding='ascii'))
                # Starts session
                elif(function == "Session"):
                    APICommand = api()
                    result = APICommand.CreateSession(conn)
                    print("Session Started")
                else:
                    print("didn't match")
                    conn.sendall("not a matching function")
        print("Connection Closed")


main()
