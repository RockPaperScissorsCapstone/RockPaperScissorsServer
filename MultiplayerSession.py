import socket
from DataBaseManager import DBManager

class MultiplayerSession:
    def __init__(self):
        print("Multiplayer started")

    def startMultiplayerSession(self, conn1, conn2):
        conn1ID = int(conn1.recv(1024).decode('ascii'))
        conn2ID = int(conn2.recv(1024).decode('ascii'))
        conn1.sendall(str(conn2ID).encode('ascii'))
        conn2.sendall(str(conn1ID).encode('ascii'))
        conn1.sendall("1".encode('ascii'))
        conn2.sendall("1".encode('ascii'))
        
        print("Multiplayer started")
        conn1wins = 0
        conn2wins = 0
        pconn1move = 4
        pconn2move = 4
        pconn1result = 3
        pconn2result = 3
        round = 1
        while conn1wins < 2 and conn2wins < 2:
            dbmconn1 = DBManager()
            dbmconn2 = DBManager()
            conn1Data = []
            conn2Data = []
            conn1Move = int(conn1.recv(1024))
            conn2Move = int(conn2.recv(1024))
            if conn1Move == conn2Move:
                conn1.sendall("0".encode('ascii'))
                conn2.sendall("0".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(2)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(2)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 2
                pconn2result = 2
            elif conn1Move == 1 and conn2Move == 2:
                conn1.sendall("-1".encode('ascii'))
                conn2.sendall("1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(0)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(1)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 0
                pconn2result = 1
                conn2wins += 1
            elif conn1Move == 2 and conn2Move == 3:
                conn1.sendall("-1".encode('ascii'))
                conn2.sendall("1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(0)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(1)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 0
                pconn2result = 1
                conn2wins += 1
            elif conn1Move == 3 and conn2Move == 1:
                conn1.sendall("-1".encode('ascii'))
                conn2.sendall("1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(0)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(1)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 0
                pconn2result = 1
                conn2wins += 1
            elif conn1Move == 1 and conn2Move == 3:
                conn1.sendall("1".encode('ascii'))
                conn2.sendall("-1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(1)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(0)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 1
                pconn2result = 0
                conn1wins += 1
            elif conn1Move == 2 and conn2Move == 1:
                conn1.sendall("1".encode('ascii'))
                conn2.sendall("-1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(1)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(0)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 1
                pconn2result = 0
                conn1wins += 1
            elif conn1Move == 3 and conn2Move == 2:
                conn1.sendall("1".encode('ascii'))
                conn2.sendall("-1".encode('ascii'))
                conn1Data.append(conn1ID)
                conn1Data.append(pconn1move)
                conn1Data.append(pconn1Result)
                conn1Data.append(conn1Move)
                conn1Data.append(1)
                conn1Data.append(round)
                dbmconn1.moveInsert(conn1Data)
                conn2Data.append(conn2ID)
                conn2Data.append(pconn2move)
                conn2Data.append(pconn2Result)
                conn2Data.append(conn2Move)
                conn2Data.append(0)
                conn2Data.append(round)
                dbmconn2.moveInsert(conn2Data)
                pconn1move = conn1Move
                pconn2move = conn2Move
                pconn1result = 1
                pconn2result = 0
                conn1wins += 1
            round += 1
        if conn1wins == 2:
            conn1.sendall("2".encode('ascii'))
            conn2.sendall("-2".encode('ascii'))
        else:
            conn1.sendall("-2".encode('ascii'))
            conn2.sendall("2".encode('ascii'))