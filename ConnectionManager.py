import socket
import threading
from Queue import myQueue
from API import api
from Assigner import Assigner


class ConnectionManager(threading.Thread):
    # Production Host
    # HOST = '172.31.47.99'

    # Nicks Test Host
    HOST = '172.31.20.135'
    PORT = 65432
    socketQue = None

    def __init__(self, que):
        threading.Thread.__init__(self)
        self.socketQue = que


    def run(self):
        print("server is up")
        threads = []
        while True:
            # Runs while there is data being sent over the socket.
            # can be picked up again at any time until the socket is released/closed.
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # s is the socket object
                # it is being given the host and port to create an endpoint
                # on the local system with which to listen to
                s.bind((self.HOST, self.PORT))
                s.listen()

                # When connection is established create a que with which to store the messages in.
                conn, addr = s.accept()
                #worker = threading.Thread(target=Assigner, args=(conn,))
                worker = Assigner(conn)
                threads.append(worker, self.socketQue)
                print("Starting worker")
                worker.start()
