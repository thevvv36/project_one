from random import randint

def display_board(board):
    print("     ",board[1] +"|"+board[2]+"|"+board[3])
    print("     ","--|---|--")
    print("     ",board[4] +"|"+board[5]+"|"+board[6])
    print("     ","--|---|--")
    print("     ",board[7] +"|"+board[8]+"|"+board[9])
    print("     ","--|---|--")



def player_choose():
    marker = ''

    while not(marker == 'x' or marker == 'o'):
        marker = input("Ready to play? choose beetwen X and O : ").upper()
        if marker == 'X':
            return ('X','O')
        else:
            return('O','X')


def ramdom_begin():

    num = randint(0,1)
    if num==0:
        return 'player1'
    else:
        return 'player2'


def put_marker(board,marker,position):
    board[position] = marke


def check_space(board,position):
    return board[position] == ' '


def check_win(board,position,marker):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    



def check_full_board(board,postion,marker):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True



def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position,marker):
        position = int(input("enter a number beetwen 1-9 : "))
        return position

def replay():
    print(" do you want to replay ?")



while True:

    theboard = [' '] * 10
    player1,player2 = player_choose()
    game_on = input("do you want to begin the game ?, enter yes or no").lower()
    if game_on == 'yes':
        game_on = True
    else:
        game_on = False


    while game_on:
        turn = radom_begin()
        print( turn +' will begin the party')
        if turn == 'player1':
            display_board(theboard)
            position = player_choice(theboard)
            put_marker(theboard,marker,position)
            if check_win():
                display_board(theboard)
                print("congratulation you win the game ")
                game_on = False
            else:
                if check_full_board(theboard):
                    display_board(theboard)
                    print("the board is full no one win ")
                    game_on = False
                else:
                    turn = 'player2'
        else:
            display_board(theboard)
            position = player_choice(theboard)
            put_marker(theboard,marker,position)
             if check_win():
                 display_board(theboard)
                 print("congratulation you win the game ")
                 game_on = False
             else:
                 if check_full_board(theboard):
                     display_board(theboard)
                     print("the board is full no one win ")
                     game_on = False
                else:
                    turn = 'player1'
