from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    marker = ''
    #keep asking player 1 to choose x or 0
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()   
    #assign player 2 the oppisite marker
    
    
    if marker == 'X':
        return ('X','O')
    elif marker == 'O':
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or #middle horizontal
    (board[7] == mark and board[8] == mark and board[9] == mark) or #top
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle vertical
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right
    (board[1] == mark and board[5] == mark and board[7] == mark) or #bottomleft to topright
    (board[7] == mark and board[5] == mark and board[3] == mark)) #topleft to bottomright

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'player 2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    #ask for a number
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Player, please choose your spot: '))
        
    return position

def replay():
    return input("Do you want to play again? ").lower().startswith('y')


print('Welcome to Tic Tac Toe!')

#while True:
while True:
    # Set the game up here
    board1 = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn +' will go first')
    play_game = input('Are you ready? Enter Yes or No. ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1 Turn
        if turn == 'player 1':
            display_board(board1)
            print('player 1:')
            position = player_choice(board1)
            place_marker(board1,player1_marker,position)
            if win_check(board1, player1_marker):
                display_board(board1)
                print ('You win!!!')
                game_on == False
            else:
                if full_board_check(board1):
                    display_board(board1)
                    print('CATSEYE!')
                    break
            turn = 'player 2'
        # Player2's turn.
        else:
            if turn == 'player 2':
                display_board(board1)
                print('player 2:')
                position = player_choice(board1)
                place_marker(board1,player2_marker,position)
                if win_check(board1, player2_marker):
                    display_board(board1)
                    print ('You win!!!')
                    game_on = False
                else:
                    if full_board_check(board1):
                        display_board(board1)
                        print('CATSEYE!')
                        break
                turn = 'player 1'
            #pass
    if not replay():
        break