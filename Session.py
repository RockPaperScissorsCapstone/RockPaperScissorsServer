#Session is currently implemented for best 2-of-3 game 
#to be applied to dummy AI
import socket
from Queue import myQueue
from DataBaseManager import DBManager
import mysql.connector
from mysql.connector import errorcode

class session:
    def __init__(self, dbm):
        self.dbm = dbm
        print("Session started")

    def startSession(self, conn):
        print("started session")
        playerWins = 0
        aiWins = 0
        pmove = 4
        presult = 3
        result = 2
        round = 1

        while (aiWins < 2 and playerWins < 2):
            playerMove = 0
            pID = conn.recv(1024)
            playerMove = conn.recv(1024)
            pID = pID.decode('ascii')
            playerMove = playerMove.decode('ascii')
            AI_input = [int(pID), int(pmove), int(presult)]
            
            aiMove = self.dbm.AI_fetch(AI_input)
            if(str.isdigit(str(aiMove))):
                return aiMove
            playerMove = int(playerMove)

            print(playerMove)
            print(aiMove)
            
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
            if(str.isdigit(str(dbmResponse))):
                return str(dbmResponse)
            pmove = playerMove
            presult = result
            print("Player Win: " + str(playerWins))
            print("AI Win: " + str(aiWins))
            if (playerWins < 2 and aiWins < 2):
                print("Keep going!")
                conn.sendall("2".encode('ascii'))
                conn.sendall(str(playerWins).encode('ascii'))
                conn.sendall(str(aiWins).encode('ascii'))
            print("send another move!")

            #print("Player move: " + playerMove ". AI move: " + aiMove)

            #conn.sendall(data)
        print("Game Over.")
        if(playerWins == 2):
            print("Player wins")
            return "1"
        else:
            print("AI wins")
            return "0"