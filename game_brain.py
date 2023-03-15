class GameBrain:
    def show_board(self, board_state):
        """Prints the current board state"""

        board = (f"{board_state['TL']} | {board_state['TM']} | {board_state['TR']}\n"
                 "----------\n"
                 f"{board_state['ML']} | {board_state['MM']} | {board_state['MR']}\n"
                 "----------\n"
                 f"{board_state['BL']} | {board_state['BM']} | {board_state['BR']}\n")

        print(board)

    def reset_board(self):
        return {"TL": 1, "TM": 2, "TR": 3,
                "ML": 4, "MM": 5, "MR": 6,
                "BL": 7, "BM": 8, "BR": 9}

    def change_turn(self, turn):
        """Changes whose turn it is from X to O or vice versa"""

        if turn == "X":
            return "O"
        elif turn == "O":
            return "X"

    def human_move(self, move, board_state, turn):
        try:
            if int(move) in board_state.values() and move != "X" and move != "O":
                for (key, value) in board_state.items():
                    if str(value) == move:
                        board_state[key] = turn

                        return True

            elif int(move) in range(0, 9):
                print("That square is already taken! Try another.")
                return False

        except ValueError:
            if move == "X" or move == "O":
                print("Remember, use the corresponding letters on the board to make your move!")
                return False

            else:
                print("Did you make a typo? Try again!")
                return False

    def is_win(self, board_state, turn):
        """Returns true if someone has won the game, and prints who has won"""

        win = False
        if board_state["TL"] == board_state["TM"] == board_state["TR"]:
            win = True
        elif board_state["ML"] == board_state["MM"] == board_state["MR"]:
            win = True
        elif board_state["BL"] == board_state["BM"] == board_state["BR"]:
            win = True
        elif board_state["TL"] == board_state["ML"] == board_state["BL"]:
            win = True
        elif board_state["TM"] == board_state["MM"] == board_state["BM"]:
            win = True
        elif board_state["TR"] == board_state["MR"] == board_state["BR"]:
            win = True
        elif board_state["TL"] == board_state["MM"] == board_state["BR"]:
            win = True
        elif board_state["TR"] == board_state["MM"] == board_state["BL"]:
            win = True

        if win:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.show_board(board_state)
            turn = self.change_turn(turn)
            print(f"Game over! {turn} is the winner!")

            return True

        else:
            return False

    def is_draw(self, board_state):
        """Returns true if the game is drawn, and prints that it is a draw"""

        draw = True
        for (key, value) in board_state.items():
            if isinstance(value, int):
                draw = False
        if draw:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.show_board(board_state)
            print(f"Game over! It's a draw!")
            return True

        else:
            return False

    def game_over(self):
        again_input = input("Would you like to play again? (Y/N): ").upper()
        if again_input != "Y":
            return True
        else:
            return False
