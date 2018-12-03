from DataBaseManager import DBManager
import csv
def main():
    autoCycle = int(input("Enter a string of moves without spaces"))
    numbOfRuns = int(input("Enter the number of games to play"))
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
    while counter < numbOfRuns:
        autoMove = listOfMoves[counter % len(listOfMoves)]
        dbm = DBManager()
        aiMove = dbm.AI_fetch([1, pmove, presult])
        if autoMove == aiMove:
            print("The script played %d and the AI played %d, the result is a draw" % (autoMove, aiMove))
            result = 2
        elif (autoMove == 1 and aiMove == 2) or (autoMove == 2 and aiMove == 3) or (autoMove == 3 and aiMove == 1):
            print("The script played %d and the AI played %d, the result is an AI victory")
            result = 0
        else:
            print("The script played %d and the AI played %d, the result is a script victory")
            result = 1
        moveInput = [1, pmove, presult, autoMove, result, counter]
        dbm2 = DBManager()
        dbm2.move_Insert(moveInput)
        pmove = autoMove
        presult = result
        counter += 1
        if result == 2:
            to_write = [counter, 0]
        elif result == 1:
            to_write = [counter, -1]
        else:
            to_write = [counter, 1]
        output_writer.writerow(to_write)
    output_file.close()
main()