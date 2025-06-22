
class game:
    def __init__(self):
        self.turn = "w"
        self.newgame()

    def newgame(self): # generates default chessboard
        self.board =  [
            ["r","k","b","q","k","b","k","r"],
            ["p" for i in range(8)],
            [" " for i in range(8)],
            [" " for i in range(8)],
            [" " for i in range(8)],
            [" " for i in range(8)],
            ["P" for i in range (8)],
            ["R","K","B","Q","K","B","K","R"]
            ]
        
        
    def valid_move(self):
        


    def turn(self):
        while True:
            from_pos = input("enter the coordinates for the piece you want to move: ").lower()
            to_pos = input("enter the coordinates for the next location: ").lower()
            try:
                for move in zip(from_pos,to_pos):
                    if move[0] in ["a","b","c","d","e","f","g","h"]:
                        continue
                    elif int(move[1:]) in range(1,9):
                        continue
                    raise ValueError
            except ValueError:
                print("invalid move")
                continue
            if self.valid_move():
                self.move()
