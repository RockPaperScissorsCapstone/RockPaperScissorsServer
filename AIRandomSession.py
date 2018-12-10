import socket
from Queue import myQueue
from DataBaseManager import DBManager
import mysql.connector
from mysql.connector import errorcode

class randomSession:
    def __init__(self, dbm):
        self.dbm = dbm
        print("Random Session started")

    def startRandomSession(self, conn):
        print("started random session")
        playerWins = 0
        aiWins = 0
        pmove = 4
        presult = 3
        result = 2
        round = 1

        code = conn.recv(1024)
        code = code.decode('ascii')
        print(code)
        while (code != '0'):
            playerMove = 0
            pID = conn.recv(1024)
            playerMove = conn.recv(1)
            pID = pID.decode('ascii')
            playerMove = playerMove.decode('ascii')
            AI_input = [int(pID), int(pmove), int(presult)]

            aiMove = self.dbm.AI_fetch(AI_input)
            if(not(str.isdigit(str(aiMove)))):
                return str(aiMove)
            playerMove = int(playerMove)
            print("Player Move: ", playerMove)
            print("AI Move: ", aiMove)

            #
            #  AI IMPLEMENTATION HERE TO SELECT MOVE
            #
            #Player Input invalid (Timeout, etc)
            if(playerMove == 0): 
                aiWins += 1
            #Player and AI Play same move, round doesn't count
            elif(playerMove == aiMove):
                result = 2
                round += 1
            elif(playerMove == 1 and aiMove == 2): #Player: rock, AI: paper
                aiWins += 1
                result = 0
                round += 1
            elif(playerMove == 1 and aiMove == 3): #Player: rock, AI: Scissors
                playerWins += 1
                result = 1
                round += 1
            elif(playerMove == 2 and aiMove == 1): #Player: Paper, AI: Rock
                playerWins += 1
                result = 1
                round += 1
            elif(playerMove == 2 and aiMove == 3): #Player: Paper, AI: Scissors
                aiWins += 1
                result = 0
                round += 1
            elif(playerMove == 3 and aiMove == 1): #Player: Scissors, AI: Rock
                aiWins += 1
                result = 0
                round += 1
            elif(playerMove == 3 and aiMove == 2): #Player: Scissors, AI: Paper
                playerWins += 1
                result = 1
                round += 1
            else:
                print("No Move Present")
            move_Input = []
            move_Input.append(pID)
            move_Input.append(pmove)
            move_Input.append(presult)
            move_Input.append(playerMove)
            move_Input.append(result)
            move_Input.append(round)
            dbmResponse = self.dbm.move_Insert(move_Input)
            if(not(str.isdigit(str(dbmResponse)))):
                return str(dbmResponse)
            pmove = playerMove
            presult = result
            print("Player Win: " + str(playerWins))
            print("AI Win: " + str(aiWins))

            conn.sendall(str(playerWins).encode('ascii'))
            conn.sendall(str(aiWins).encode('ascii'))

            print(code)
            code = conn.recv(1024)
            code = code.decode('ascii')

        print(code)
        return "Play Against AI Random End"