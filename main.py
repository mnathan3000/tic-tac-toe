from random import choice, randint
from time import sleep
from game_brain import GameBrain
from computer_brain import ComputerBrain

game_brain = GameBrain()
computer_brain = ComputerBrain()

play_again = True
x_points = 0
o_points = 0

print("Welcome to Noughts and Crosses!")
sleep(1)
how_many_players = input("Would you like to play against the computer (C) or another human (H)? ").lower()

### GAME VS HUMAN ###

if how_many_players == "h":
    turn = choice(["X", "O"])
    print("Decide who's going to be noughts and who's going to be crosses. You have 5 seconds.\n")
    sleep(1)

    while play_again:
        game_on = True
        board_state = game_brain.reset_board()
        turn = game_brain.change_turn(turn)

        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOK. This time, {turn} goes first!\n")
        game_brain.show_board(board_state)
        move = input("Where would you like to go? Type 1-9: ").upper()

        while game_on:
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if game_brain.human_move(move, board_state, turn):
                turn = game_brain.change_turn(turn)

            game_brain.show_board(board_state)

            ### CHECK IF GAME IS WON OR DRAWN ###

            if game_brain.is_win(board_state, turn):
                game_on = False
                turn = game_brain.change_turn(turn)
                if turn == "X":
                    x_points += 1
                elif turn == "O":
                    o_points += 1
                print(f"That makes the scores: \nX: {x_points} \nO: {o_points}")
                if game_brain.game_over():
                    play_again = False

            elif game_brain.is_draw(board_state):
                game_on = False
                print(f"That makes the scores: \nX: {x_points} \nO: {o_points}")
                if game_brain.game_over():
                    play_again = False

            else:
                move = input(f"{turn}'s Turn! Where would you like to go? ").upper()



### GAME VS COMPUTER ###

elif how_many_players == "c":
    turn = choice(["X", "O"])
    print(computer_brain.show_robot())
    print("Bleep blorp. I am the Tic-Tac-Tobot 3000.\n")
    sleep(1)
    print("No human can equal my Tic-Tac-Total mastery of this game.\n")
    sleep(2)

    difficulty_set = True

    while difficulty_set:

        difficulty = input("Please set my difficulty level between 1 (easiest) and 20 (hardest): ")
        if int(difficulty) not in range(1, 21):
            sleep(1)
            print("That's not a number between 1 and 20! Clearly you're not so smart - I'll set the difficulty to 1.")
            sleep(2)
            difficulty = 1
        difficulty = int(difficulty)

        print("\nI'll play as X and you play as O.")
        sleep(1)

        play_again = True

        while play_again:

            board_state = game_brain.reset_board()

            game_on = True

            if turn == "O":
                print("\nYou go first this time.\n")
                human_turn = True

            else:
                print("\nI'll go first this time.\n")
                human_turn = False

            sleep(1)

            while game_on:

                ### HUMAN MOVE ###

                if human_turn:
                    game_brain.show_board(board_state)
                    move = input(f"Where would you like to go? Type 1-9: ").upper()
                    if game_brain.human_move(move, board_state, turn):
                        turn = game_brain.change_turn(turn)
                        human_turn = False

                ###COMPUTER MOVE###

                else:
                    sleep(0.5)
                    print("\n\nTic-Tac-Tobot 3000's turn:")
                    makes_random_move = randint(1, difficulty)
                    if makes_random_move == difficulty:
                        board_state[computer_brain.random_move(board_state)] = turn
                    else:
                        board_state[computer_brain.best_move(board_state)] = turn
                    turn = game_brain.change_turn(turn)
                    human_turn = True

                ### CHECK IF WIN OR DRAW ###

                if game_brain.is_win(board_state, turn):
                    game_on = False
                    turn = game_brain.change_turn(turn)
                    if turn == "X":
                        x_points += 1
                        computer_brain.winning_speech()
                    elif turn == "O":
                        o_points += 1
                        computer_brain.losing_speech()
                    print(f"That makes the scores: \nX: {x_points} \nO: {o_points}")

                    turn = game_brain.change_turn(turn)
                    if game_brain.game_over():
                        play_again = False
                        difficulty_set = False
                    else:
                        change_difficulty = input("Would you like to change difficulty? (Y/N): ").upper()
                        if change_difficulty == "Y":
                            play_again = False



                elif game_brain.is_draw(board_state):
                    game_on = False
                    computer_brain.drawing_speech()
                    print(f"That makes the scores: \nX: {x_points} \nO: {o_points}")
                    game_brain.change_turn(turn)
                    if game_brain.game_over():
                        play_again = False
                        difficulty_set = False
                    else:
                        change_difficulty = input("Would you like to change difficulty? (Y/N): ").upper()
                        if change_difficulty == "Y":
                            play_again = False

else:
    print("That wasn't a C or an H! You don't deserve to play Noughts and Crosses.")

print("Goodbye!")
