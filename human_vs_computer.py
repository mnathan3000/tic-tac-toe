from game_brain import GameBrain
from computer_brain import ComputerBrain
from time import sleep
from random import randint
from typing import Union


def human_vs_computer(game_brain: GameBrain, computer_brain: ComputerBrain) -> Union[str, None]:
    """Plays one round of Noughts and Crosses human vs computer.
    Returns "X" or "O" if there is a winner, or None if it is a draw"""

    game_brain.reset_board()
    game_brain.change_turn()

    if game_brain.turn == "O":
        print("\nYou go first this time.\n")
        computer_brain.human_turn = True

    else:
        print("\nI'll go first this time.\n")
        computer_brain.human_turn = False

    while True:

        if computer_brain.human_turn:
            print(game_brain.show_board())
            move = input(f"Where would you like to go? Type 1-9: ").upper()
            if game_brain.is_move_legal(move):
                game_brain.make_human_move(move)
                game_brain.change_turn()
                computer_brain.human_turn = False

        else:
            sleep(1)
            print("\n\nTic-Tac-Tobot 3000's turn:")

            if computer_brain.makes_random_move():
                computer_brain.random_move(game_brain)
            else:
                game_brain.board_state[computer_brain.best_move(game_brain)] = game_brain.turn
            game_brain.change_turn()
            computer_brain.human_turn = True

        if game_brain.is_win():
            if game_brain.turn == "X":
                computer_brain.winning_speech()
                return game_brain.turn
            elif game_brain.turn == "O":
                computer_brain.losing_speech()
                return game_brain.turn

        elif game_brain.is_draw():
            computer_brain.drawing_speech()
            return None
