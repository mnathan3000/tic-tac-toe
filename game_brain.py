class GameBrain:

    def __init__(self):

        self.board_state = {"TL": 1, "TM": 2, "TR": 3,
                            "ML": 4, "MM": 5, "MR": 6,
                            "BL": 7, "BM": 8, "BR": 9}

        self.turn = "X"
        self.x_points = 0
        self.o_points = 0

    def show_board(self) -> str:
        """Returns the current board state as a string"""

        return (f"{self.board_state['TL']} | {self.board_state['TM']} | {self.board_state['TR']}\n"
                 "----------\n"
                 f"{self.board_state['ML']} | {self.board_state['MM']} | {self.board_state['MR']}\n"
                 "----------\n"
                 f"{self.board_state['BL']} | {self.board_state['BM']} | {self.board_state['BR']}\n")

    def reset_board(self):
        """Returns an empty board as a dictionary"""

        self.board_state = {"TL": 1, "TM": 2, "TR": 3,
                            "ML": 4, "MM": 5, "MR": 6,
                            "BL": 7, "BM": 8, "BR": 9}

    def change_turn(self):
        """Changes whose turn it is from X to O or vice versa. Returns X or O as a string."""

        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"

    def make_human_move(self, move: str):
        """Inserts X or O into the board state dictionary at the position given by move variable"""

        for (key, value) in self.board_state.items():
            if str(value) == move:
                self.board_state[key] = self.turn

    def is_move_legal(self, move: str) -> bool:
        """Returns True if attempted move is legal and false if it is not"""

        try:
            if int(move) in self.board_state.values() and move != "X" and move != "O":
                return True

            elif int(move) in range(0, 9):
                print("That square is already taken! Try another.")

        except ValueError:
            if move == "X" or move == "O":
                print("Remember, use the corresponding letters on the board to make your move!")

            else:
                print("Did you make a typo? Try again!")
        return False

    def is_win(self) -> bool:
        """Returns True if someone has won the game, prints the board and who has won"""

        win = False
        if self.board_state["TL"] == self.board_state["TM"] == self.board_state["TR"]:
            win = True
        elif self.board_state["ML"] == self.board_state["MM"] == self.board_state["MR"]:
            win = True
        elif self.board_state["BL"] == self.board_state["BM"] == self.board_state["BR"]:
            win = True
        elif self.board_state["TL"] == self.board_state["ML"] == self.board_state["BL"]:
            win = True
        elif self.board_state["TM"] == self.board_state["MM"] == self.board_state["BM"]:
            win = True
        elif self.board_state["TR"] == self.board_state["MR"] == self.board_state["BR"]:
            win = True
        elif self.board_state["TL"] == self.board_state["MM"] == self.board_state["BR"]:
            win = True
        elif self.board_state["TR"] == self.board_state["MM"] == self.board_state["BL"]:
            win = True

        if win:
            print("\n" * 15)
            print(self.show_board())
            self.change_turn()
            print(f"Game over! {self.turn} is the winner!")

            return True
        return False

    def is_draw(self) -> bool:
        """Returns true if the game is drawn, prints the board and prints that it is a draw"""

        draw = True
        for (key, value) in self.board_state.items():
            if isinstance(value, int):
                draw = False
        if draw:
            print("\n" * 20)
            print(self.show_board())
            print(f"Game over! It's a draw!")
            return True
        return False

    def add_point(self):
        if self.turn == "X":
            self.x_points += 1
        elif self.turn == "O":
            self.o_points += 1
    def player_wants_to_continue(self) -> bool:
        """Asks if the player would like to play again. Returns True if yes and False if no"""

        user_response = input("Would you like to play again? (Y/N): ").upper()
        return user_response == "Y"
