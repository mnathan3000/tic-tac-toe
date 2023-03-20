from random import choice, randint
from time import sleep
from game_brain import GameBrain
from typing import Union, Callable


class ComputerBrain:

    def __init__(self):
        self.difficulty = None
        self.human_turn = True

    def show_robot(self) -> str:
        return r"""

               _______
             _/       \_
            / |       | \
           /  |__   __|  \
          |__/((o| |o))\__|
          |      | |      |
          |\     |_|     /|
          | \           / |
           \| /  ___  \ |/
            \ | / _ \ | /
             \_________/
              _|_____|_
         ____|_________|____
        /                   \ 
                                """

    def set_difficulty(self):
        """Changes difficulty attribute to input. Difficulty attribute is an integer."""
        if self.difficulty is None:
            speech = "Please set my difficulty level between 1 (easiest) and 20 (hardest): "
        else:
            print("Too much for you, was I?")
            speech = "What difficulty would you like this time? " \
                     "Set it between 1 (easiest) and 20 (hardest): "
            while True:
                difficulty_input = \
                    input(speech)
                try:
                    if int(difficulty_input) not in range(1, 21):
                        sleep(1)
                        print("That's not a number between 1 and 20! Try again. Do better.\n")
                        sleep(2)
                    else:
                        self.difficulty = int(difficulty_input)
                        return

                except ValueError:
                    print("That wasn't a number, was it? Humans are just so inferior. Try again.\n")
                    sleep(1)

    def start_game(self, game_brain: GameBrain):
        game_brain.turn = choice(["X", "O"])
        print(self.show_robot())
        print("Bleep blorp. I am the Tic-Tac-Tobot 3000.\n")
        sleep(1)
        print("No human can equal my Tic-Tac-Total mastery of this game.\n")
        sleep(2)

        self.set_difficulty()
        print("\nI'll play as X and you play as O.")
        sleep(1)

    def random_move(self, game_brain: GameBrain):
        """Plays a random, legal move. Enters the value into the board state dictionary
        attribute"""
        possible_moves = []
        for (key, value) in game_brain.board_state.items():
            if isinstance(value, int):
                possible_moves.append(key)
        game_brain.board_state[choice(possible_moves)] = "X"

    def best_move(self, game_brain: GameBrain):
        """Returns the board state dictionary key for the best valid move as a string"""

        # Starting moves

        if all(isinstance(value, int) for value in game_brain.board_state.values()):
            return "TL"
        elif game_brain.board_state == {"TL": 1, "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6,
                                        "BL": 7, "BM": 8, "BR": 9}:
            return "TL"

        # Win conditions

        if game_brain.board_state["TL"] == "X":
            if game_brain.board_state["TM"] == "X" and game_brain.board_state["TR"] != "O":
                return "TR"
            elif game_brain.board_state["TR"] == "X" and game_brain.board_state["TM"] != "O":
                return "TM"
            elif game_brain.board_state["ML"] == "X" and game_brain.board_state["BL"] != "O":
                return "BL"
            elif game_brain.board_state["BL"] == "X" and game_brain.board_state["ML"] != "O":
                return "ML"
            elif game_brain.board_state["MM"] == "X" and game_brain.board_state["BR"] != "O":
                return "BR"
            elif game_brain.board_state["BR"] == "X" and game_brain.board_state["MM"] != "O":
                return "MM"

        if game_brain.board_state["MM"] == "X":
            if game_brain.board_state["ML"] == "X" and game_brain.board_state["MR"] != "O":
                return "MR"
            elif game_brain.board_state["MR"] == "X" and game_brain.board_state["ML"] != "O":
                return "ML"
            elif game_brain.board_state["TM"] == "X" and game_brain.board_state["BM"] != "O":
                return "BM"
            elif game_brain.board_state["BM"] == "X" and game_brain.board_state["TM"] != "O":
                return "TM"
            elif game_brain.board_state["BL"] == "X" and game_brain.board_state["TR"] != "O":
                return "TR"
            elif game_brain.board_state["TR"] == "X" and game_brain.board_state["BL"] != "O":
                return "BL"

        if game_brain.board_state["BL"] == "X":
            if game_brain.board_state["BM"] == "X" and game_brain.board_state["BR"] != "O":
                return "BR"
            elif game_brain.board_state["BR"] == "X" and game_brain.board_state["BM"] != "O":
                return "BM"

        if game_brain.board_state["BR"] == "X":
            if game_brain.board_state["BM"] == "X" and game_brain.board_state["BL"] != "O":
                return "BL"
            elif game_brain.board_state["MR"] == "X" and game_brain.board_state["TR"] != "O":
                return "TR"
            elif game_brain.board_state["TR"] == "X" and game_brain.board_state["MR"] != "O":
                return "MR"

        if game_brain.board_state["TR"] == "X" and game_brain.board_state["MR"] == "X" and \
                game_brain.board_state["BR"] != "O":
            return "BR"

        # Dont lose conditions

        if game_brain.board_state["TL"] == "O":
            if game_brain.board_state["TM"] == "O" and game_brain.board_state["TR"] != "X":
                return "TR"
            elif game_brain.board_state["TR"] == "O" and game_brain.board_state["TM"] != "X":
                return "TM"
            elif game_brain.board_state["ML"] == "O" and game_brain.board_state["BL"] != "X":
                return "BL"
            elif game_brain.board_state["BL"] == "O" and game_brain.board_state["ML"] != "X":
                return "ML"
            elif game_brain.board_state["MM"] == "O" and game_brain.board_state["BR"] != "X":
                return "BR"

        if game_brain.board_state["MM"] == "O":
            if game_brain.board_state["ML"] == "O" and game_brain.board_state["MR"] != "X":
                return "MR"
            elif game_brain.board_state["MR"] == "O" and game_brain.board_state["ML"] != "X":
                return "ML"
            elif game_brain.board_state["MR"] == "O" and game_brain.board_state["ML"] != "X":
                return "ML"
            elif game_brain.board_state["BM"] == "O" and game_brain.board_state["TM"] != "X":
                return "TM"
            elif game_brain.board_state["BL"] == "O" and game_brain.board_state["TR"] != "X":
                return "TR"
            elif game_brain.board_state["TR"] == "O" and game_brain.board_state["BL"] != "X":
                return "BL"
            elif game_brain.board_state["TM"] == "O" and game_brain.board_state["BM"] != "X":
                return "BM"

        if game_brain.board_state["BL"] == "O":
            if game_brain.board_state["BM"] == "O" and game_brain.board_state["BR"] != "X":
                return "BR"
            elif game_brain.board_state["BR"] == "O" and game_brain.board_state["BM"] != "X":
                return "BM"
            elif game_brain.board_state["ML"] == "O" and game_brain.board_state["TL"] != "X":
                return "TL"

        if game_brain.board_state["BR"] == "O":
            if game_brain.board_state["BM"] == "O" and game_brain.board_state["BL"] != "X":
                return "BL"
            elif game_brain.board_state["MR"] == "O" and game_brain.board_state["TR"] != "X":
                return "TR"

            elif game_brain.board_state["TR"] == "O" and game_brain.board_state["MR"] != "X":
                return "MR"

        if game_brain.board_state["TR"] == "O" and game_brain.board_state["MR"] == "O" and \
                game_brain.board_state["BR"] != "X":
            return "BR"

        # Strategy

        if game_brain.board_state == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6,
                                      "BL": 7, "BM": 8, "BR": 9}:
            return "BR"
        if game_brain.board_state == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6,
                                      "BL": "O", "BM": 8, "BR": "X"}:
            return "TR"
        if game_brain.board_state == {"TL": "X", "TM": 2, "TR": "O", "ML": 4, "MM": "O", "MR": 6,
                                      "BL": 7, "BM": 8, "BR": "X"}:
            return "BL"
        if game_brain.board_state == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": 5, "MR": 6,
                                      "BL": 7, "BM": 8, "BR": "O"}:
            return "BL"
        if game_brain.board_state == {"TL": "X", "TM": 2, "TR": 3, "ML": "O", "MM": 5, "MR": 6,
                                      "BL": "X", "BM": 8, "BR": "O"}:
            return "TR"
        if game_brain.board_state == {"TL": "O", "TM": 2, "TR": 3, "ML": 4, "MM": "X", "MR": 6,
                                      "BL": 7, "BM": 8, "BR": "O"}:
            return "BM"
        if game_brain.board_state == {"TL": 1, "TM": 2, "TR": "O", "ML": 4, "MM": "X", "MR": 6,
                                      "BL": "O", "BM": 8, "BR": 9}:
            return "BM"

        if game_brain.board_state["TL"] == "X" and game_brain.board_state["BR"] == 9:
            return "BR"

        if game_brain.board_state["TL"] == "X" and game_brain.board_state["BR"] == "X":
            if game_brain.board_state["BL"] == 7:
                return "BL"
            elif game_brain.board_state["TR"] == 3:
                return "TR"

        if game_brain.board_state["MM"] == 5:
            return "MM"

        else:
            return self.random_move(game_brain)

    def makes_random_move(self) -> bool:
        """Returns True if computer is going to make a random move,
        or False if it will make the best move"""
        makes_random_move = randint(1, self.difficulty)
        if makes_random_move == self.difficulty:
            return True
        return False

    def winning_speech(self):
        """Prints robot face and victory speech"""

        print(self.show_robot())
        print(choice(["Well, that tick-tac-toes all the boxes",
                      "You got tic-tac-tOWNED!",
                      "You know, I used to practice on a magnetic tic-tac-toe board. It...didn't go well.",
                      "I'm a tic-tac-pro!",
                      "Way to tic-tac-go, me!",
                      "Remember, don't ever cross me. Or nought me, for that matter.",
                      "I deserve a pat on the back. Shame that I'm just a bunch of code."]))

    def losing_speech(self):
        """Prints robot face and defeat speech"""

        print(self.show_robot())
        print(choice(["That was Tic-Whack-Toe. I can't believe you beat me!",
                      "It was all for nought!",
                      "Well, now I'm cross.",
                      "What a tic-tacky way to win.",
                      "Tic-tac-NOOOOOO!",
                      "How did I tic-tac-throw that one away?!",
                      "I'll tic-tac-show you!",
                      "Tic-tac-woe is me!"]))

    def drawing_speech(self):
        """Prints robot face and draw speech"""

        print(self.show_robot())
        print(choice(["Jolly good tic-tac-show! Care for another?",
                      "And they say computers can't draw. Silly humans!",
                      "Looks like we've ended up tic-tac-toe to toe.",
                      "You are a worthy tic-tac-foe. Congratulations."]))
