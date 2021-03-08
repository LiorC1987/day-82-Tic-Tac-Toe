from random import randint

blocks = []
play_again = True
game = ""


def start_game():
    global blocks
    blocks = []
    for n in range(0, 9):
        blocks += f"{n + 1}"


start_game()



def game_display():
    global game
    game = f"""
 {blocks[0]} | {blocks[1]} | {blocks[2]}
-----------
 {blocks[3]} | {blocks[4]} | {blocks[5]}
-----------
 {blocks[6]} | {blocks[7]} | {blocks[8]}  """
    return print(game)


def check_for_winner(player):
    global winner_declared
    global play_again
    if blocks[0] == blocks[1] == blocks[2] or \
            blocks[3] == blocks[4] == blocks[5] or \
            blocks[6] == blocks[7] == blocks[8] or \
            blocks[0] == blocks[3] == blocks[6] or \
            blocks[1] == blocks[4] == blocks[7] or \
            blocks[2] == blocks[5] == blocks[8] or \
            blocks[0] == blocks[4] == blocks[8] or \
            blocks[2] == blocks[4] == blocks[6]:
        if player == "player 1":
            print("Player 1 has won!")
            winner_declared = True
            ask_play_again = input("Would you like to play again? (Y/N)").upper()
            if ask_play_again == "N":
                play_again = False
        else:
            print("Player 2 has won!")
            winner_declared = True
            ask_play_again = input("Would you like to play again? (Y/N)").upper()
            if ask_play_again == "N":
                play_again = False
    if blocks[0] != str(1) and \
        blocks[1] != str(2) and \
        blocks[2] != str(3) and \
        blocks[3] != str(4) and \
        blocks[4] != str(5) and \
        blocks[5] != str(6) and \
        blocks[6] != str(7) and \
        blocks[7] != str(8) and \
        blocks[8] != str(9):
        print("It's a tie!")
        winner_declared = True
        ask_play_again = input("Would you like to play again? (Y/N)").upper()
        if ask_play_again == "N":
            play_again = False


### PLAY AGAINST ANOTHER PERSON

while play_again:
    start_game()
    game_display()
    winner_declared = False
    while not winner_declared:
        legitimate_spot = False
        while not legitimate_spot:
            try:
                player_one_play = int(input("Player 1, choose a spot to mark an X on this board:"))
                if blocks[player_one_play - 1] == "X" or blocks[player_one_play - 1] == "O":
                    print("this spot is already taken, choose another spot")
                else:
                    blocks[player_one_play - 1] = "X"
                    legitimate_spot = True
            except (IndexError, ValueError):
                print("This is not a legitimate choice. Try again.")
        game_display()
        check_for_winner("player 1")
        if not winner_declared:
            legitimate_spot = False
            while not legitimate_spot:
                try:
                    player_two_play = int(input("Player 2, choose a spot to mark an X on this board:"))
                    if blocks[player_two_play - 1] == "O" or blocks[player_two_play - 1] == "O":
                        print("this spot is already taken, choose another spot")
                    else:
                        blocks[player_two_play - 1] = "O"
                        legitimate_spot = True
                except (IndexError, ValueError):
                    print("This is not a legitimate choice. Try again.")
            game_display()
            check_for_winner("player 2")

#### PLAY AGAINST AI
# game_display()
# while not winner_declared:
#     player_one_play = int(input("Player 1, choose a spot to mark an X on this board:"))
#     blocks[player_one_play - 1] = "X"
#
#     check_for_winner("player 1")
#     if not winner_declared:
#         acceptable_spot = False
#         while not acceptable_spot:
#             player_two_play = randint(1, 9)
#             if str(player_two_play) == blocks[player_two_play - 1]:
#                 acceptable_spot = True
#         blocks[player_two_play - 1] = "O"
#         game_display()
#         check_for_winner("player 2")
