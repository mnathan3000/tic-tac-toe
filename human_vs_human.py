from typing import Union
from game_brain import GameBrain


def human_vs_human(turn: str, game_brain: GameBrain) -> Union[str, None]:
    """Returns "X" or "O" if there is a winner, or None if it is a draw"""

    board_state = game_brain.reset_board()
    turn = game_brain.change_turn(turn)

    print(f"\n" * 20)
    print(f"OK. This time, {turn} goes first!\n")
    game_brain.show_board(board_state)
    move = input("Where would you like to go? Type 1-9: ").upper()

    while True:
        print(f"\n" * 10)
        if game_brain.human_move(move, board_state, turn):
            turn = game_brain.change_turn(turn)

        game_brain.show_board(board_state)

        if game_brain.is_win(board_state, turn):
            turn = game_brain.change_turn(turn)
            return turn

        elif game_brain.is_draw(board_state):
            return None

        else:
            move = input(f"{turn}'s Turn! Where would you like to go? ").upper()