# game board
theboared = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
             'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
             'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

print('the positions are as follows:\n')
print('top-l | top-m | top-r')
print('------+-------+-------')
print('mid-l | mid-m | mid-r')
print('------+-------+------')
print('low-l | low-m | low-r\n\n')

#function to print the board on the screen
def boardprint(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['low-l']+'|'+board['low-m']+'|'+board['low-r'])
boardprint(theboared)

#function to update the board whenever a player takes the turn
def updateboard(a,x,board):
    c=0
    for i in board.keys():
        if i==x and board[x]==' ':
            board[x]=a
            break
        elif i==x and board[x]!=' ':
            print('wrong position entered; pre-occupied space ')
            return 1
    if i!=x:
        print("wrong position entered")
        return 1
    return 0

#function to check if match is draw
def checkdraw(board):
    for i in board.values():
        if i==' ':
            return 0
    return 1

# function to check if the game is over or not
def check(board):
    
    #condition for 'X' to win
    if ((board['top-l']=='X' and board['top-m']=='X' and board['top-r']=='X') or (board['mid-l']=='X' and board['mid-m']=='X' and board['mid-r']=='X') or(
        board['low-l']=='X' and board['low-m']=='X' and board['low-r']=='X') or (board['top-l']=='X' and board['mid-m']=='X' and board['low-r']=='X') or(
        board['top-r']=='X' and board['mid-m']=='X' and board['low-l']=='X') or (board['top-l']=='X' and board['mid-l']=='X' and board['low-l']=='X' ) or(
        board['top-m']=='X' and board['mid-m']=='X' and board['low-m']=='X') or (board['top-r']=='X' and board['mid-r']=='X' and board['low-r']=='X')):
        print('X wins')
        return 1
    
    #condition for 'O' to win
    elif ((board['top-l']=='O' and board['top-m']=='O' and board['top-r']=='O') or (board['mid-l']=='O' and board['mid-m']=='O' and board['mid-r']=='O') or(
        board['low-l']=='O' and board['low-m']=='O' and board['low-r']=='O') or (board['top-l']=='O' and board['mid-m']=='O' and board['low-r']=='O') or(
        board['top-r']=='O' and board['mid-m']=='O' and board['low-l']=='O') or (board['top-l']=='O' and board['mid-l']=='O' and board['low-l']=='O') or(
        board['top-m']=='O' and board['mid-m']=='O' and board['low-m']=='O') or (board['top-r']=='O' and board['mid-r']=='O' and board['low-r']=='O')):
        print('O wins')
        return 1
    
    #condition of draw
    elif checkdraw(board)==1:
        print('draw match')
        return 1
    #if no one wins
    else:
        return 0
        
#driver part of the code
print('who will start first, X or O ??')
a= input()
if a=='X':    
    print('chose a position for X using indeces')
elif a=='O':
    print('chose a position for O using indeces')
else:
    while a:
        print('wrong choice entered enter a valid one:')
        a= input()
        if a=='X' or a=='O':
            break
    
        
while a:
    x= input('enter position: ')
    turn = updateboard(a,x,theboared)
    if turn == 1 and a=='X':
        a='O'
    elif turn ==1 and a=='O':
        a='X'
    boardprint(theboared)
    t=check(theboared)
    if t== 1 :
        print('game over!!')
        input("press enter key")
        break
    elif a=='X':
        print('turn of O')
        a='O'
    elif a=='O':
        print('turn of X')
        a='X'
