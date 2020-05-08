"""Congratulations on making it to your first milestone!

You've already learned a ton and are ready to work on a real project.

Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

    2 players should be able to play the game (both sitting at the same computer)
    The board should be printed out every time a player makes a move
    You should be able to accept input of the player position and then place a symbol on the board

Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.

There are 4 Jupyter Notebooks related to this assignment:

    This Assignment Notebook
    A "Walkthrough Steps Workbook" Notebook
    A "Complete Walkthrough Solution" Notebook
    An "Advanced Solution" Notebook

I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
HAVE FUN!"""



import random


def display_board(board):

    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_input():
    player1=(input("Player 1 - Ingrese si desea jugar con 'X' o con 'O': ")).upper()

    while (player1!="X" and player1!="O"):
        player1=input("Player 1 - Ingrese si desea jugar con 'X' o con 'O': ")

    if player1=="X":
        player2="O"
    else:
        player2="X"
    return (player1, player2)


def position_marker(board):

    pos=int(input("Elige la posición (1-9): "))

    while pos not in [1,2,3,4,5,6,7,8,9, ] or not space_check(board, pos):
        pos=int(input("Elige la posición (1-9): "))

    return pos


def place_marker(board, marker, position):
    board[position]=marker
   


def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[3]==mark and board[5]==mark and board[7]==mark))


def choose_first():
    ran=random.randint(0,1)
    if ran==0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
    return board[position]==" "


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def replay():
    rep=(input("Quieren jugar nuevamente? (Si - No): ")).lower()
    while(rep!="si" and rep!="no"):
          rep=input("Quieren jugar nuevamente? (Si - No): ")
    if rep == "si":
        return True
    else:
        return False



print("Bienvenido al Ta Te Ti!!")

while True:

    board = [" "]*10

    player1_m, player2_m = player_input()

    choose = choose_first()

    print(f"{choose} juega primero.")

    comenzar = True
    
    while comenzar:
        
        #Player 1
        if choose == "Player 1":
            display_board(board)
            position = position_marker(board)
            place_marker(board, player1_m, position)
            
            if win_check(board, player1_m):
                display_board(board)
                print("Felicitaciones!! Player 1 es el ganador!!")
                comenzar = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Es un empate!! Vuelvan a intentar!!")
                    break
                else:
                    choose = "Player 2"
        
        #Player 2
        else:
            display_board(board)
            position = position_marker(board)
            place_marker(board, player2_m, position)
            
            if win_check(board, player2_m):
                display_board(board)
                print("Felicitaciones!! Player 2 es el ganador!!")
                comenzar = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Es un empate!! Vuelvan a intentar!!")
                    break
                else:
                    choose = "Player 1"
    if not replay():
        break                    