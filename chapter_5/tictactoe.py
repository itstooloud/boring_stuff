# just a database storing a value for each box in the grid


theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}

# function to print the board

def printboard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + " | " + board['top-R'])
    print('- + - + - ')
    print(board['mid-L'] + ' | ' + board['mid-M'] + " | " + board['mid-R'])
    print('- + - + - ')
    print(board['low-L'] + ' | ' + board['low-M'] + " | " + board['low-R'])


printboard(theBoard)

turn = 'X'

for i in range(9):
    printboard(theBoard)
    print('Input move for player ' + turn + ":")
    move = input()x
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(theBoard)

#gonna save this because I have a feeling we're going to come back to it
# and check to see if a player has won and also not allow for moves over old moves



    
