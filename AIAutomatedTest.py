from DataBaseManager import DBManager
from DBConnectors import DBConnectors
import csv
def main():
    autoCycle = int(input("Enter a string of moves without spaces: "))
    numbOfRuns = int(input("Enter the number of games to play: "))
    listOfMoves = []
    output_file = open("output.csv", "w", newline="")
    output_writer = csv.writer(output_file)
    output_file.truncate
    while autoCycle % 10 != autoCycle:
        listOfMoves.append(autoCycle % 10)
        autoCycle = int(autoCycle / 10)
    listOfMoves.append(autoCycle)
    listOfMoves.reverse()
    presult = 4
    pmove = 4
    result = 0
    counter = 0
    wins = 0
    losses = 0
    ties = 0
    output_writer.writerow(["Round", "Player Move", "AI move", "Result"])
    dbcp = DBConnectors()
    dbm = DBManager(dbcp)
    while counter < numbOfRuns:
        autoMove = listOfMoves[counter % len(listOfMoves)]
        aiMove = dbm.AI_fetch([19, pmove, presult])
        if autoMove == aiMove:
            print("The script played %d and the AI played %d, the result is a draw" % (autoMove, aiMove))
            result = 2
        elif (autoMove == 1 and aiMove == 2) or (autoMove == 2 and aiMove == 3) or (autoMove == 3 and aiMove == 1):
            print("The script played %d and the AI played %d, the result is an AI victory" % (autoMove, aiMove))
            result = 0
        else:
            print("The script played %d and the AI played %d, the result is an AI loss" % (autoMove, aiMove))
            result = 1
        moveInput = [19, pmove, presult, autoMove, result, counter]
        dbm.move_Insert(moveInput)
        pmove = autoMove
        presult = result
        counter += 1
        to_write = [counter]
        if autoMove == 1:
            to_write.append("Rock")
        elif autoMove == 2:
            to_write.append("Paper")
        else:
            to_write.append("Scissors")
        if aiMove == 1:
            to_write.append("Rock")
        elif aiMove == 2:
            to_write.append("Paper")
        else:
            to_write.append("Scissors")
        if result == 2:
            to_write.append("Tie")
            ties += 1
        elif result == 1:
            to_write.append("Loss")
            losses += 1
        else:
            to_write.append("Win")
            wins += 1
        output_writer.writerow(to_write)
    output_writer.writerow(["Wins", wins])
    output_writer.writerow(["Loses", losses])
    output_writer.writerow(["Ties", ties])
    dbm.autoMoveRemover()
    output_file.close()
main()