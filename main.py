import os
import random
import time

grid = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]
available_grid = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
# positions V
# "0", "1", "2",
# "3", "4", "5",
# "6", "7", "8"

x = "x"
o = "o"

player_team = ""
ai_team = ""
winner = ""
current_turn = None
count = 0

game_running = True

def main():
    global current_turn

    pick_team()
    os.system("PAUSE")
    os.system("CLS")

    if player_team == "o":
        current_turn = ai_team
    elif player_team == "x":
        current_turn = player_team

    draw_board(grid)
    while game_running:
        if current_turn == player_team:
            num = int(input("1-9: "))
            place_shape(player_team, num)
        if current_turn == ai_team:
            time.sleep(1)
            ai_plays(grid)
    else:
        current_turn = None

def place_shape(team, spot):
    os.system("CLS")
    global current_turn

    spot -= 1

    while spot < 0 or spot > 8 and team == player_team:
        os.system("CLS")
        draw_board(grid)
        spot = int(input("Not a spot. 1-9: "))
    else: pass

    if grid[spot] == "-":
        available_grid.remove(spot+1) #'occupy' the available space

        grid[spot] = str(team)
        draw_board(grid)

        check_win(grid, spot)
    else:
        if current_turn == ai_team:
            ai_plays(grid)
        else:
            draw_board(grid)
            spot = int(input("Already taken. 1-9: "))

    if current_turn == ai_team:
        current_turn = player_team
    if current_turn == player_team:
        current_turn = ai_team

def ai_plays(board): # ai makes a turn
    global current_turn
    if current_turn == ai_team and game_running:
        print(current_turn == ai_team)

        print("attemping to place")
        print("the current team is " + str(current_turn))

        choice = random.randint(1, 9)
        print(choice)
        place_shape(ai_team, choice)
        current_turn = player_team

def check_win(board, spot_to_check):
    global winner
    global game_running

    #horizontal
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = str(board[0])
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = str(board[3])
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = str(board[6])

    #vertical
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = str(board[0])
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = str(board[1])
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = str(board[2])

    #diagonal
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = str(board[0])
    if board[6] == board[4] == board[2] and board[6] != "-":
        winner = str(board[6])

    if len(available_grid) == 0 and winner == None:
        print("You have tied!")

    if winner != "":
        print(winner.upper() + " is the winner!")
        game_running = False

def draw_board(board):
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])

def pick_team():
    global player_team
    global ai_team

    choices = [x, o]

    random_choice1 = random.choice(choices)
    random_choice2 = None

    if random_choice1 == x:
        random_choice2 = o
    else:
        random_choice2 = x

    player_team = random_choice1
    ai_team = random_choice2

    print("You are playing as " + player_team + ".\n")

main()