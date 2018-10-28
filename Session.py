#Session is currently implemented for best 2-of-3 game 
#to be applied to dummy AI
import socket
from Queue import myQueue
from DataBaseManager import DBManager
from datetime import date

class session:
    myQue = None
    def __init__(self):
        print("Session started")
        self.myQue = myQueue()

    def startSession(self, conn):
        playerWins = 0
        aiWins = 0
        pmove = 4
        presult = 3
        dateToday = str(date.today())
        dbm = DBManager()

        while (aiWins < 2 or playerWins < 2):
            playerMove = 0
            pID = conn.recv(1024)
            playerMove = conn.recv(1024)
            pID = pID.decode('ascii')
            AIid = 99999
            pMove = conn.decode('ascii')
            AI_input = []
            AI_input.append(int(pID))
            AI_input.append(pmove)
            AI_input.append(presult)
            self.myQue.addtoq(data)
            aiMove = dbm.AI_fetch(AI_input)
            #
            #  AI IMPLEMENTATION HERE TO SELECT MOVE
            #
            #Player Input invalid (Timeout, etc)
            if(playerMove == 0): 
                aiWins += 1
            #Player and AI Play same move, round doesn't count
            if(playerMove == aiMove):
                result = 2
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 1 and aiMove == 2): #Player: rock, AI: paper
                aiWins += 1
                result = 0
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 1 and aiMove == 3): #Player: rock, AI: Scissors
                playerWins += 1
                result = 1
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 2 and aiMove == 1): #Player: Paper, AI: Rock
                playerWins += 1
                result = 1
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 2 and aiMove == 3): #Player: Paper, AI: Scissors
                aiWins += 1
                result = 0
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 3 and aiMove == 1): #Player: Scissors, AI: Rock
                aiWins += 1
                result = 0
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            elif(playerMove == 3 and aiMove == 2): #Player: Scissors, AI: Paper
                playerWins += 1
                result = 1
                move_Input = []
                move_Input.append(pID)
                move_Input.append(pmove)
                move_Input.append(presult)
                move_Input.append(playerMove)
                move_Input.append(result)
                dbm.move_Insert(move_Input)
                pmove = playerMove
                presult = result
            else:
                print("No Move Present")

            #print("Player move: " + playerMove ". AI move: " + aiMove)

            #conn.sendall(data)
            print("Game Over.")
            if(playerWins == 2):
                winnerId = pID
                matchHistoryInfo = []
                matchHistoryInfo.append(pID)
                matchHistoryInfo.append(AIid)
                matchHistoryInfo.append(winnerId)
                matchHistoryInfo.append(dateToday)
                dbm.updateMatchHistory(matchHistoryInfo)

                print("Player wins")
                return 1
            else:
                print("AI wins")
                winnerId = AIid
                matchHistoryInfo = []
                matchHistoryInfo.append(pID)
                matchHistoryInfo.append(AIid)
                matchHistoryInfo.append(winnerId)
                matchHistoryInfo.append(dateToday)
                dbm.updateMatchHistory(matchHistoryInfo)
                return 0

