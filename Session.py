# Session is currently implemented for best 2-of-3 game
# to be applied to dummy AI


class Session:


    def __init__(self):
        print("Session started")

    def startSession(conn):
        playerwins = 0
        aiWins = 0

        while (aiWins < 2 or playerWins < 2):
            data = conn.recv(1024)
            myQue.addtoq(data)
            aiMove = -1
            #
            #  AI IMPLEMENTATION HERE TO SELECT MOVE
            #
            playerMove = data.decode('cp437')

            # Player Input invalid (Timeout, etc)
            if (playerMove == 0):
                aiWins += 1
            # Player and AI Play same move, round doesn't count
            if(playerMove == aiMove):
                break
            elif(playerMove == 1 and aiMove == 2):  # Player: rock, AI: paper
                aiWins += 1
            elif(playerMove == 1 and aiMove == 3):  # Player: rock, AI: Scissors
                playerWins += 1
            elif(playerMove == 2 and aiMove == 1):  # Player: Paper, AI: Rock
                playerWins += 1
            elif(playerMove == 2 and aiMove == 3):  # Player: Paper, AI: Scissors
                aiWins += 1
            elif(playerMove == 3 and aiMove == 1):  # Player: Scissors, AI: Rock
                aiWins += 1
            elif(playerMove == 3 and aiMove == 2):  # Player: Scissors, AI: Paper
                playerWins += 1
            else:
                print("No Move Present")

            print("Player move: " + playerMove + ". AI move: " + aiMove)

            # conn.sendall(data)

        print("Game Over.")
        if (playerwins == 2):
            print("Player wins")
            return 1
        else:
            print("AI wins")
            return 0
