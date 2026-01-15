'''we will make the board using dictionary in which keys will be the location'''

theBoard = {
    '7': '', '8': '', '9': '',
    '4': '', '5': '', '6': '',
    '1': '', '2': '', '3': ''
}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printboard(board):
    """Prints the current state of the board"""
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        if theBoard.get(move) == '':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled or invalid.\nTry again.")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != '':
                printboard(theBoard)
                print("\nGame Over.\n**** " + turn + " won. ****")
                break

        if count == 9:
            printboard(theBoard)
            print("\nGame Over.\nIt's a Tie!!")
            break

        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play again? (y/n): ")
    if restart.lower() == 'y':
        for key in board_keys:
            theBoard[key] = ''
        game()


if __name__ == "__main__":
    game()
