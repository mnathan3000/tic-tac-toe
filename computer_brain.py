from random import choice


class ComputerBrain:

    def random_move(self, board_state):
        possible_moves = []
        for (key, value) in board_state.items():
            if isinstance(value, int):
                possible_moves.append(key)
        return (choice(possible_moves))

    def best_move(self, bs):

        ### STARTING MOVES ###

        if all(isinstance(value, int) for value in bs.values()):
            return "TL"
        elif bs == {"TL": 1, "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6, "BL": 7, "BM": 8, "BR": 9}:
            return "TL"

        ### WIN CONDITIONS ###

        if bs["TL"] == "X":
            if bs["TM"] == "X" and bs["TR"] != "O":
                return "TR"
            elif bs["TR"] == "X" and bs["TM"] != "O":
                return "TM"
            elif bs["ML"] == "X" and bs["BL"] != "O":
                return "BL"
            elif bs["BL"] == "X" and bs["ML"] != "O":
                return "ML"
            elif bs["MM"] == "X" and bs["BR"] != "O":
                return "BR"
            elif bs["BR"] == "X" and bs["MM"] != "O":
                return "MM"

        if bs["MM"] == "X":
            if bs["ML"] == "X" and bs["MR"] != "O":
                return "MR"
            elif bs["MR"] == "X" and bs["ML"] != "O":
                return "ML"
            elif bs["TM"] == "X" and bs["BM"] != "O":
                return "BM"
            elif bs["BM"] == "X" and bs["TM"] != "O":
                return "TM"
            elif bs["BL"] == "X" and bs["TR"] != "O":
                return "TR"
            elif bs["TR"] == "X" and bs["BL"] != "O":
                return "BL"

        if bs["BL"] == "X":
            if bs["BM"] == "X" and bs["BR"] != "O":
                return "BR"
            elif bs["BR"] == "X" and bs["BM"] != "O":
                return "BM"

        if bs["BR"] == "X":
            if bs["BM"] == "X" and bs["BL"] != "O":
                return "BL"
            elif bs["MR"] == "X" and bs["TR"] != "O":
                return "TR"
            elif bs["TR"] == "X" and bs["MR"] != "O":
                return "MR"

        if bs["TR"] == "X" and bs["MR"] == "X" and bs["BR"] != "O":
            return "BR"

        ### DON'T LOSE CONDITIONS ###

        if bs["TL"] == "O":
            if bs["TM"] == "O" and bs["TR"] != "X":
                return "TR"
            elif bs["TR"] == "O" and bs["TM"] != "X":
                return "TM"
            elif bs["ML"] == "O" and bs["BL"] != "X":
                return "BL"
            elif bs["BL"] == "O" and bs["ML"] != "X":
                return "ML"
            elif bs["MM"] == "O" and bs["BR"] != "X":
                return "BR"

        if bs["MM"] == "O":
            if bs["ML"] == "O" and bs["MR"] != "X":
                return "MR"
            elif bs["MR"] == "O" and bs["ML"] != "X":
                return "ML"
            elif bs["MR"] == "O" and bs["ML"] != "X":
                return "ML"
            elif bs["BM"] == "O" and bs["TM"] != "X":
                return "TM"
            elif bs["BL"] == "O" and bs["TR"] != "X":
                return "TR"
            elif bs["TR"] == "O" and bs["BL"] != "X":
                return "BL"
            elif bs["TM"] == "O" and bs["BM"] != "X":
                return "BM"

        if bs["BL"] == "O":
            if bs["BM"] == "O" and bs["BR"] != "X":
                return "BR"
            elif bs["BR"] == "O" and bs["BM"] != "X":
                return "BM"
            elif bs["ML"] == "O" and bs["TL"] != "X":
                return "TL"

        if bs["BR"] == "O":
            if bs["BM"] == "O" and bs["BL"] != "X":
                return "BL"
            elif bs["MR"] == "O" and bs["TR"] != "X":
                return "TR"

            elif bs["TR"] == "O" and bs["MR"] != "X":
                return "MR"

        if bs["TR"] == "O" and bs["MR"] == "O" and bs["BR"] != "X":
            return "BR"

        ### STRATEGY ###

        if bs == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6, "BL": 7, "BM": 8, "BR": 9}:
            return "BR"
        if bs == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": "O", "MR": 6, "BL": "O", "BM": 8, "BR": "X"}:
            return "TR"
        if bs == {"TL": "X", "TM": 2, "TR": "O", "ML": 4, "MM": "O", "MR": 6, "BL": 7, "BM": 8, "BR": "X"}:
            return "BL"
        if bs == {"TL": "X", "TM": 2, "TR": 3, "ML": 4, "MM": 5, "MR": 6, "BL": 7, "BM": 8, "BR": "O"}:
            return "BL"
        if bs == {"TL": "X", "TM": 2, "TR": 3, "ML": "O", "MM": 5, "MR": 6, "BL": "X", "BM": 8, "BR": "O"}:
            return "TR"
        if bs == {"TL": "O", "TM": 2, "TR": 3, "ML": 4, "MM": "X", "MR": 6, "BL": 7, "BM": 8, "BR": "O"}:
            return "BM"
        if bs == {"TL": 1, "TM": 2, "TR": "O", "ML": 4, "MM": "X", "MR": 6, "BL": "O", "BM": 8, "BR": 9}:
            return "BM"

        if bs["TL"] == "X" and bs["BR"] == 9:
            return "BR"

        if bs["TL"] == "X" and bs["BR"] == "X":
            if bs["BL"] == 7:
                return "BL"
            elif bs["TR"] == 3:
                return "TR"

        if bs["MM"] == 5:
            return "MM"



        else:
            return self.random_move(bs)

    def show_robot(self):
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

    def winning_speech(self):
        print(self.show_robot())
        print(choice(["Well, that tick-tac-toes all the boxes",
                      "You got tic-tac-tOWNED!",
                      "You know, I used to practice on a magnetic tic-tac-toe board. It...didn't go well.",
                      "I'm a tic-tac-pro!",
                      "Way to tic-tac-go, me!",
                      "Remember, don't ever cross me. Or nought me, for that matter.",
                      "I deserve a pat on the back. Shame that I'm just a bunch of code."]))

    def losing_speech(self):
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
        print(self.show_robot())
        print(choice(["Jolly good tic-tac-show! Care for another?",
                      "And they say computers can't draw. Silly humans!",
                      "Looks like we've ended up tic-tac-toe to toe.",
                      "You are a worthy tic-tac-foe. Congratulations."]))
