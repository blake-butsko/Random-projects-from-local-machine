# 05/20/22 Blake Butsko
# I had just taken the cisco internship assesment and they had a question on there where the coordinates of a queen chess piece and a random piece

def is_diagonal(cord_x1,cord_y1,cord_x2,cord_y2):
    # just slope
    return ((cord_y2-cord_y1)/(cord_x2-cord_x1)) == 1

def check_attack_queen(cord_x1,cord_y1,cord_x2,cord_y2):
    if cord_x1 == cord_x2 or cord_y1 == cord_y2 or is_diagonal(cord_x1,cord_y1,cord_x2,cord_y2):
        return True
    return False
    
    # might be replaced by a method used to show the possible moves (all the space you could move would be highlighted and then it just checks if there's a piece on one of the possible moves)
    # I'm imagining light that gets stopped by pieces then the ones you can attack have a red border around their position
    # this method just sees if it's a viable attack

# make queen object and pawn object and update their coordinates as they move across the board

class piece:
    def __init__(self, x, y):
        self.cord_x = x #could name self.x but they named it self.cord_x in the assesment
        self.cord_y = y
    def set_cord(self, x, y):
        self.cord_x = x
        self.cord_y = y
    def get_cord(self):
        return [self.x, self.y]
        # eventually will be used with 

# class queen(piece):
    # all this really does it set how it can move (attack can be done either by checking if the space selected has a piece on it or something else)
    # so I should just somehow organize the moves for each piece type in a more efficent way bc I feel like it'd take too much space to define each one of them in a class
    # if we define it in it's own function we can just pass it into the constructor but then it's like the same thing as each having their own class


queen = piece(4,5)
pawn = piece(7, 7)
# print(pawn.cord_x)

# make array for chess board - it doesn't work but I'm tired - supposed to be an 8 by 8 array where the astrix represents the position of the queen
board = [[' ']*8]*8
# board[queen.cord_x][queen.cord_y] = '*'
board[0][5] = '*'
y = 0
# for x in board:
#     print(y)
#     y+=1
#     print(x)
for x in range(len(board)):
    board[x]
# print(board)