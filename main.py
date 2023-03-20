from random import choice
from time import sleep
from game_brain import GameBrain
from computer_brain import ComputerBrain
from human_vs_human import human_vs_human
from human_vs_computer import human_vs_computer

game_brain = GameBrain()
computer_brain = ComputerBrain()

print("Welcome to Noughts and Crosses!")
sleep(1)
how_many_players = input("Would you like to play against the computer (C) or another human (H)? ").upper()

# Game vs human

if how_many_players == "H":
    game_brain.turn = choice(["X", "O"])
    print("Decide who's going to be noughts and who's going to be crosses. You have 5 seconds.\n")
    sleep(5)

    while True:

        winner = human_vs_human(game_brain)

        if winner is not None:
            game_brain.add_point()
        print(f"That makes the scores: \n"
              f"X: {game_brain.x_points} \n"
              f"O: {game_brain.o_points}")

        if not game_brain.player_wants_to_continue():
            break

# Game vs computer

elif how_many_players == "C":

    computer_brain.start_game(game_brain)

    while True:

        winner = human_vs_computer(game_brain, computer_brain)

        if winner is not None:
            game_brain.add_point()
        print(f"That makes the scores: \n"
              f"X: {game_brain.x_points} \n"
              f"O: {game_brain.o_points}")

        if game_brain.player_wants_to_continue():
            player_wants_to_change_difficulty = \
                input("OK, would you like to change the difficulty? (Y/N): ").upper()
            if player_wants_to_change_difficulty == "Y":
                computer_brain.set_difficulty()
            else:
                continue

        else:
            break




else:
    print("That wasn't a C or an H! You don't deserve to play Noughts and Crosses.")

print("Goodbye!")
