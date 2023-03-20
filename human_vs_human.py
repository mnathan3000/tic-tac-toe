from typing import Union
from game_brain import GameBrain


def human_vs_human(game_brain: GameBrain) -> Union[str, None]:
    """Plays one round of Noughts and Crosses human vs human.
    Returns "X" or "O" if there is a winner, or None if it is a draw"""

    game_brain.reset_board()
    game_brain.change_turn()

    print(f"\n" * 20)
    print(f"OK. This time, {game_brain.turn} goes first!\n")
    print(game_brain.show_board())
    move = input("Where would you like to go? Type 1-9: ").upper()

    while True:
        print(f"\n" * 10)
        if game_brain.is_move_legal(move):
            game_brain.make_human_move(move)
            game_brain.change_turn()

        print(game_brain.show_board())

        if game_brain.is_win():
            return game_brain.turn

        elif game_brain.is_draw():
            return None

        else:
            move = input(f"{game_brain.turn}'s Turn! Where would you like to go? ").upper()