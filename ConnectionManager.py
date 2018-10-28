import socket
from Queue import myQueue
from API import api
HOST = '172.31.47.99'
PORT = 65432


def main():
    print("server is up")
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            myQue = myQueue()
            result = None
            function = ''
            endData = 1
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    myQue.addtoq(data)
                    if (data.decode('ascii') == "end"):
                        conn.sendall(data)
                        break
                    print(data.decode('ascii'))
                    conn.sendall(data)
                function = (myQue.removefromq()).decode('ascii')
                print("function = " + function)
                print("reached")
                if(function == "CreateAccount"):
                    APICommand = api()
                    result = APICommand.CreateAccount(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode(encoding='ascii'))
                elif(function == "GetAccountInfo"):
                    APICommand = api()
                    result = APICommand.GetAccountInfo(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode('ascii'))
                elif(function == "Login"):
                    APIcommand = api()
                    result = APIcommand.Login(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode(encoding='ascii'))
                elif(function == "AIGame"):
                    APICommand = api()
                    result = APICommand.AI_fetch(myQue)
                    print("result: " + result)
                    conn.sendall(result.encode(encoding='ascii'))
                # Start session
                elif(function == "Session"):
                    APICommand = api()
                    result = APICommand.CreateSession(conn)
                    print("Session Started")
                else:
                    print("didn't match")
                    conn.sendall("not a matching function")
                conn.sendall(result.encode('ascii'))

        print("Connection Closed")


main()
